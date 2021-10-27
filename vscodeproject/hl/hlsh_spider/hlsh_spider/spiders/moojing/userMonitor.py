from requests.api import request
import scrapy
from hlsh_spider.settings import API_KEY
import json
from fake_useragent  import UserAgent

class UserMonitorSpider(scrapy.Spider):

    name = 'user_monitor'
    start_urls = ["https://market.moojing.com/api/marked" ]
    
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    headers['MOOJING-APIKEY']=API_KEY
    # print("header:%s"%headers)

    custom_settings = {
        'ITEM_PIPELINES':{'hlsh_spider.pipelines.moojingPipelines.UserMonitorPipeline': 300}
    }
    def start_requests(self):

        for url in self.start_urls:
            print(url)
            test_request = scrapy.Request(url, headers=self.headers, method='GET',callback=self.parse)
            print("test_request:%s"%test_request)
            yield test_request


    def parse(self, response):

        result = json.loads(response.text)['result']
        data = result['data']
        for val in data:
            item = {
                'model':self.name,
                'url':response.url,
                'platform': val['platform'],
                'brand_name': val['brand_name'],
                'standard': val['standard'],
                'brand_id': val['brand_id'],
                'platname': val['platname'],
                'ts_start': val['ts_range'][0][0],
                'ts_end': val['ts_range'][0][1],
                'category_id': val['category_id'],
                'type': val['type'],
                'category_name': val['category_name']    
            }
            # print(item)
            # break
            yield item


# class SiteSummarySpider(scrapy.Spider):

#     name = 'sitesummary'
#     # 构造url列表
#     start_urls = ["https://market.moojing.com/api/platform/jd/cats/15901/brands/all/summary" ]
    
#     ua = UserAgent()
#     headers = {'User-Agent': ua.random}
#     headers['MOOJING-APIKEY']=API_KEY
#     # print("header:%s"%headers)

#     custom_settings = {
#         'ITEM_PIPELINES':{'hlsh_spider.pipelines.moojingPipelines.UserMonitorPipeline': 300}
#     }
#     def start_requests(self):

#         for url in self.start_urls:
#             print(url)
#             test_request = scrapy.Request(url, headers=self.headers, method='GET',callback=self.parse)
#             print("test_request:%s"%test_request)
#             yield test_request


#     def parse(self, response):

#         result = json.loads(response.text)['result']
#         # data = result['data']
#         # for val in result:
#         item = {
#             'model':self.name,
#             'url':response.url,
#             'result': result
                
#         }
#         # print(item)
#         # break
#         yield item