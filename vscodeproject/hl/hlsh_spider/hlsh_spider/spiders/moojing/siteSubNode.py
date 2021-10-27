from requests.api import request
import scrapy
from hlsh_spider.settings import API_KEY
import json
from fake_useragent import UserAgent
from hlsh_spider.utils.moojingUrl import ConcatUrl
from urllib.parse import urlparse, parse_qs
import pendulum
import math


class SiteSubNodeBrandSpider(scrapy.Spider):
    print(pendulum.now())
    name = 'site_sub_node_brand'
    urls = ConcatUrl(is_history=False, is_time=True, model_type='list', type='brand').set_site_all_urls()
    # urls = ['https://market.moojing.com/api/platform/jd/cats/1320/brands/all/list?start=2021-05&type=brand']

    start_urls = urls
    page_size = 100
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    headers['MOOJING-APIKEY'] = API_KEY
    # print("header:%s"%headers)

    custom_settings = {
        'ITEM_PIPELINES': {'hlsh_spider.pipelines.moojingPipelines.SiteSubNodeBrandPipeline': 400}
    }

    def start_requests(self):

        for url in self.start_urls:
            # print(url)
            test_request = scrapy.Request(url, headers=self.headers, method='GET', callback=self.parse)
            # print("test_request:%s"%test_request)
            yield test_request
            # break

    def parse(self, response):

        result = json.loads(response.text)['result']

        count = result['count']
        for i in range(0, int(math.ceil(count / self.page_size))):
            # print(response.url)
            url = response.url + '&page={}&page_size={}'.format(str(i + 1), str(self.page_size))
            # print(url)
            yield scrapy.Request(url, headers=self.headers, method='GET', callback=self.parse_detail)

    def parse_detail(self, response):

        result = json.loads(response.text)['result']
        url = urlparse(response.url)
        data = result['data']
        query = parse_qs(url.query)
        for val in data:
            item = {
                'model': self.name,
                'url': response.url,
                'platform': response.url.split('/')[5],
                'category_id': val['category_id'],
                'brand_id': val['brand_id'],
                'brand_name': val['brand_name'],
                'avg_price': val['avg_price'],
                'item_num': val['item_num'],
                'market_share': val['market_share'],
                'qoq': val['qoq'],
                'sale': val['sale'],
                'shop_num': val['shop_num'],
                'sold': val['sold'],
                'yoy': val['yoy'],
                'month': query['start'][0],
                'create_time': pendulum.now().to_date_string()
            }
            # print(item)
            # break
            yield item
            # break
