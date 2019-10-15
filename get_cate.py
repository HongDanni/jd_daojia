# -*-coding:utf8 -*-
import requests

ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
headers = {'User-Agent': ua}

def get_cate(url):
    res = requests.get(url, headers=headers)
    with open('cate2.txt', 'a') as f:
        f.write(res.text)

if __name__ == '__main__':
    url_store = 'https://daojia.jd.com/client?lat=22.56705&lng=113.95371&city_id=1607&deviceToken=b2e951ed-e72e-4a9a-b9ca-cd69348c3337&deviceId=b2e951ed-e72e-4a9a-b9ca-cd69348c3337&channel=wx_xcx&platform=5.0.0&platCode=H5&appVersion=5.0.0&xcxVersion=3.6.2&appName=paidaojia&deviceModel=appmodel&functionId=station%2FgetStationDetail&isForbiddenDialog=false&isNeedDealError=false&isNeedDealLogin=false&body=%7B%22storeId%22%3A%2211653731%22%2C%22skuId%22%3A%22%22%2C%22orgCode%22%3A%2281372%22%2C%22activityId%22%3A%22%22%2C%22promotionType%22%3A%22%22%2C%22lgt%22%3A113.95371%2C%22lat%22%3A22.56705%7D&afsImg=&business='
    get_cate(url_store)
