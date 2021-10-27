# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from twisted.enterprise import adbapi
import re
from pymysql import OperationalError, InterfaceError, DataError, InternalError, IntegrityError
from pymysql.cursors import DictCursor
import pendulum

class MysqlPipeline:
    
    def __init__(self, spider, settings):
        self.spider = spider
        
        self.dbpool = adbapi.ConnectionPool('pymysql',
            host = settings.get('MYSQL_HOST', '127.0.0.1'),
            port = settings.get('MYSQL_PORT', 3306),
            user = settings.get('MYSQL_USER', 'username'),
            passwd = settings.get('MYSQL_PASSWD', 'password'),
            db = settings.get('MYSQL_DB', 'test'),
            charset = settings.get('MYSQL_CHARSET', 'utf8'), #utf8mb4
            
            cursorclass = DictCursor
        )
        self.mysql_reconnect_wait = settings.get('MYSQL_RECONNECT_WAIT', 60)
        self.mysql_item_list_limit = settings.get('MYSQL_ITEM_LIST_LIMIT', 30)
        self.item_list = []


    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            spider = crawler.spider,
            settings = crawler.settings
        )


    def close_spider(self, spider):
        self._sql(list(self.item_list))
        # spider入库记录写入数据库，要写的逻辑！！！
        print(pendulum.now())
        print(spider.name)
        print('插入数据库结束！！！！')


    def process_item(self, item, spider):
        self.item_list.append(item)
        
        if len(self.item_list) >= self.mysql_item_list_limit:
            spider.log('item_list: %s'%len(self.item_list))
            self._sql(list(self.item_list))
            self.item_list.clear()

        return item


    def sql(self, txn, item_list):
        raise NotImplementedError('Subclass of MyMySQLPipeline must implement the sql() method')


    def _sql(self, item_list, retrying=False):
        d = self.dbpool.runInteraction(self.sql, item_list)
        d.addCallback(self.handle_result, item_list)
        d.addErrback(self.handle_error, item_list, retrying)
        

    def handle_result(self, result, item_list):
        self.spider.logger.info('{} items inserted with retcode {}'.format(len(item_list), result))


    def handle_error(self, failure, item_list, retrying):
        # https://twistedmatrix.com/documents/18.7.0/api/twisted.python.failure.Failure.html
        # r = failure.trap(pymysql.err.InternalError)

        args = failure.value.args
        
        # <class 'pymysql.err.OperationalError'> (1045, "Access denied for user 'username'@'localhost' (using password: YES)")
        # <class 'pymysql.err.OperationalError'> (2013, 'Lost connection to MySQL server during query ([Errno 110] Connection timed out)')
        # <class 'pymysql.err.OperationalError'> (2003, "Can't connect to MySQL server on '127.0.0.1' ([WinError 10061] 由于目标计算机积极拒绝，无法连接。)")
        # <class 'pymysql.err.InterfaceError'> (0, '')    # after crawl started: sudo service mysqld stop
        if failure.type in [OperationalError, InterfaceError]:
            if not retrying:
                self.spider.logger.info('MySQL: exception {} {} \n{}'.format(
                                        failure.type, args, item_list))            
                self.spider.logger.debug('MySQL: Trying to recommit in %s sec'%self.mysql_reconnect_wait)
                
                # self._sql(item_list)
                # https://twistedmatrix.com/documents/12.1.0/core/howto/time.html
                from twisted.internet import task
                from twisted.internet import reactor
                task.deferLater(reactor, self.mysql_reconnect_wait, self._sql, item_list, True)
            else:
                self.spider.logger.warn('MySQL: exception {} {} \n{}'.format(
                                        failure.type, args, item_list))

            return

        # <class 'pymysql.err.DataError'> (1264, "Out of range value for column 'position_id' at row 2")
        # <class 'pymysql.err.InternalError'> (1292, "Incorrect date value: '1977-06-31' for column 'release_day' at row 26")
        elif failure.type in [DataError, InternalError]:
            m_row = re.search(r'at\s+row\s+(\d+)$', args[1])
            row = m_row.group(1)
            item = item_list.pop(int(row) - 1)
            self.spider.logger.warn('MySQL: {} {} exception from item {}'.format(failure.type, args, item))

            self._sql(item_list)
            return
            
        # <class 'pymysql.err.IntegrityError'> (1048, "Column 'name' cannot be null") films 43894
        elif failure.type in [IntegrityError]:    
            m_column = re.search(r"Column\s'(.+)'", args[1])
            column = m_column.group(1)
            some_items = [item for item in item_list if item[column] is None]
            self.spider.logger.warn('MySQL: {} {} exception from some items: \n{}'.format(
                                failure.type, args, some_items))

            self._sql([item for item in item_list if item[column] is not None])
            return
        
        else:
            self.spider.logger.error('MySQL: {} {} unhandled exception from item_list: \n{}'.format(
                                failure.type, args, item_list))

            return