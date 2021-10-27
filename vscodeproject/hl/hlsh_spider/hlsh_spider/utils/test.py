import re
import requests
import urllib
import json
import pendulum
from requests.api import get

API_KEY = 'F7C2D07C32BF1724AA27BE665DA7E823'

def get_data(url):
    r = requests.get(url, headers={'MOOJING-APIKEY': API_KEY})
    return json.loads(r.text)

def put_data(url, params):
    r = requests.put(url, data=urllib.urlencode(params), headers={'MOOJING-APIKEY': API_KEY})
    return json.loads(r.text)

def delete_data(url, params):
    r = requests.delete(url, data=urllib.urlencode(params), headers={'MOOJING-APIKEY': API_KEY})
    return json.loads(r.text)

def param_tuple_dic(url,**kwargs):
    url = url + '?'
    for k, v in kwargs.items():
        url = url + k + '=' + v + '&'
    url = url[:-1]
    print(url)

def data_flatten(key,val,con_s='_',basic_types=(str,int,float,bool,complex,bytes)):
    if isinstance(val, dict):
        for ck,item in val.items():
            yield from data_flatten(con_s.join([key,ck]).lstrip('_'),item)
    elif isinstance(val, list):
        for item in val:
            yield from data_flatten(key,item)
            yield str(key).lower()
    elif isinstance(val, basic_types) or val is None:
        yield str(key).lower(),val


if __name__ == '__main__':
    from urllib.parse import urlparse,urlsplit,parse_qs,parse_qsl
    url = 'https://market.moojing.com/api/cats_tree?plat=tmall'
    # url = 'https://market.moojing.com/api/platform/jd/cats/1320/brands/all/list?start=2021-05&type=brand&page=1&page_size=100'
    result = get_data(url)
    t = data_flatten('first',result['result']['childrenList'] )
    count = 0
    for i in t:
        count += 1
        if count > 10:
            break
        print(i)
            
    # import math
    # count = 3
    # for i in range(0,int(math.ceil(2/2))):
    #     print(i+1)