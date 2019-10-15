# -*-coding:utf-8 -*-
import requests
import json
from urllib.parse import quote
import csv
import time

ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
headers = {'User-Agent': ua}

def get_product(cateid2, catename1, catename2):
    # 根据二级类目ID：cateid2来拼接url
    body = {
        "storeId": "11653731",  # 对应cate.txt文件里的stationNo字段信息
        "orgCode": "81372",  # orgCode字段信息
        "skuId": "",
        "catIds": [{"catId": cateid2, "type": 2}]}
    body = json.dumps(body)
    body = quote(body)

    url_cate = 'https://daojia.jd.com/client?lat=22.51424&lng=113.93068&city_id=1607&deviceToken=b2e951ed-e72e-4a9a-b9ca-cd69348c3337&deviceId=b2e951ed-e72e-4a9a-b9ca-cd69348c3337&channel=wx_xcx&platform=5.0.0&platCode=H5&appVersion=5.0.0&xcxVersion=3.6.2&appName=paidaojia&deviceModel=appmodel&functionId=storeIndexSearch%2FsearchByCategory&isForbiddenDialog=false&isNeedDealError=false&isNeedDealLogin=false&body={}&afsImg=&business=undefined'.format(body)
    res = requests.get(url_cate, headers=headers)
    txt = json.loads(res.text)

    searchResultVOList = txt['result']['searchCatResultVOList'][0]['searchResultVOList']
    # 以一级类目名字（catename1）给csv表格命名
    filename = '{}.csv'.format(catename1)
    csvfile = open(filename, 'a')
    writer = csv.writer(csvfile)
    # 写入标题
    writer.writerow(['商品名称', '价格(单位:元)', '月销量', '图片', '二级类目', '一级类目'])
    # 写入内容
    for product in searchResultVOList:
        name = product['skuName']  # 商品名称
        img = product['imgUrl']  # 商品图片
        price = product['realTimePrice']  # 商品价格
        sale = product['monthSales']  # 商品月销量
        writer.writerow([name, price, sale, img, catename2, catename1])
    csvfile.close()

if __name__ == '__main__':
    # 读取cate.txt文件
    with open('cate.txt', 'r') as f:
        content = f.read()
        cateList = json.loads(content)['result']['cateList']
        for cate in cateList:
            childCategoryList = cate['childCategoryList']
            for chileCate in childCategoryList:
                user_action = json.loads(chileCate['user_action'])
                # 获得一、二级类目的ID和名称
                cateid1 = user_action['cateid1']
                cateid2 = user_action['cateid2']
                catename1 = user_action['catename1']
                catename2 = user_action['catename2']
                # 排除掉促销、满减等的商品分类
                if cateid2[0] != '#':
                    # 调用get_product()
                    get_product(cateid2, catename1, catename2)
                    time.sleep(5)



