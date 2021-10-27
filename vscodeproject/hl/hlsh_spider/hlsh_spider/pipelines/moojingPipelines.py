from hlsh_spider.utils.basePipelines import MysqlPipeline


class UserMonitorPipeline(MysqlPipeline):

    def sql(self, txn, item_list):
        return txn.executemany("""
            INSERT INTO test (
                model, url, platform, brand_name, standard, brand_id, 
                platname, ts_start, ts_end, category_id, type, category_name)
            VALUES (
                %(model)s, %(url)s, %(platform)s, %(brand_name)s, %(standard)s, 
                %(brand_id)s, %(platname)s, %(ts_start)s, %(ts_end)s, %(category_id)s, %(type)s, %(category_name)s)
        """, item_list)


class SiteSubNodeBrandPipeline(MysqlPipeline):
    #
    def sql(self, txn, item_list):
        return txn.executemany("""
            INSERT INTO test_brand (
                model, url, platform, category_id, brand_id, brand_name, 
                avg_price, item_num, market_share, qoq, sale, shop_num,
                sold, yoy, month, create_time)
            VALUES (
                %(model)s, %(url)s, %(platform)s, %(category_id)s, %(brand_id)s, 
                %(brand_name)s, %(avg_price)s, %(item_num)s, %(market_share)s, %(qoq)s, %(sale)s, %(shop_num)s,
                %(sold)s, %(yoy)s, %(month)s, %(create_time)s)
        """, item_list)
