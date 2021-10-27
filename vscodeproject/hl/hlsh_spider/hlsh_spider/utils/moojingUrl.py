# 拼接魔镜url
from re import S
import pandas as pd
from requests.models import requote_uri
from sqlalchemy import create_engine
import pendulum

class ConcatUrl:

    def __init__(self, is_history=False,is_time=True, model_type='hot_items', *args, **kwargs):
        # 是否需要获取所有历史数据
        self.is_history = is_history

        self.is_time = is_time # 是否有时间参数
        self.model_type = model_type
        self.args = args
        self.kwargs = kwargs

    def set_site_all_urls(self):
        # 原生类目的url拼接
        urls = []
        today = pendulum.now()
        time = today.subtract(months=1)
        result = self.get_base_info()
        for index, row in result.iterrows():
            base_url = 'https://market.moojing.com/api/platform/{}/cats/{}/brands/{}/{}'\
            .format(row['platform'], row['category_id'], row['brand_id'], self.model_type)

            if self.is_time:
                if self.is_history:
                    month_range = self.get_month_range(today,row['ts_start'],row['ts_end'])

                    for month in month_range:
                        url = base_url
                        url = url+'?start={}'.format(month)
                        # print(base_url)
                        if self.kwargs:
                            query_url = self.set_query(url)
                            urls.append(query_url)
                        else:
                            urls.append(url)
                else:
                    if time.month< 10:
                        url = base_url
                        url = url+'?start={}'.format(str(time.year)+'-0'+str(time.month))
                        if self.kwargs:
                            query_url = self.set_start_query(url)
                            urls.append(query_url)
                        else:
                            urls.append(url)
                    else:

                        url = base_url
                        url = url+'?start={}'.format(str(time.year)+'-'+str(time.month))
                        if self.kwargs:
                            query_url = self.set_start_query(url)
                            urls.append(query_url)
                        else:
                            urls.append(url)
                        # break
                    # pass
            else:
                    if self.kwargs:
                        query_url = self.set_query(base_url)
                        urls.append(query_url)
                    else:
                        urls.append(base_url)

        return urls


    def get_base_info(self):

        # 获取catid,plat,brandid

        con = create_engine('mysql+pymysql://hlsh:Lc3&xaOE@121.37.136.201:3338/hlsh_test')
        result = pd.read_sql_query("select platform, brand_id, ts_start, ts_end, category_id from test", con=con).drop_duplicates(subset=None, keep='first')
        return result


    def get_month_range(self,today,start_year_month,end_year_month):
        
        dts = []

        start_split = start_year_month.split('-')
        start_year = start_split[0]
        start_month = start_split[1]

        if today.subtract(months=1).month <= int(start_month):

            period = pendulum.period(today.subtract(months=1), pendulum.parse(end_year_month))

            for dt in period.range('months'):
                dts.append(dt.to_date_string()[:7])

        else:

            period = pendulum.period(pendulum.parse(start_year_month), pendulum.parse(end_year_month))

            for dt in period.range('months'):
                dts.append(dt.to_date_string()[:7])

        return dts
 
    def set_start_query(self, url):
        # 添加URL的query部分，就是？问号之后的
        for k, v in self.kwargs.items():
            url = url + '&' + k + '=' + v 
        return url

    def set_query(self, url):
        # 添加URL的query部分，就是？问号之后的
        url = url + '?'
        for k, v in self.kwargs.items():
            url = url  + k + '=' + v + '&'
        return url[:-1]

if __name__ == '__main__':
    concaturl = ConcatUrl(type='brand',start='2021-01')
    result = concaturl.set_query('https://market.moojing.com/api/platform/tmall/cats/16/brands/all/list')
    print( result )