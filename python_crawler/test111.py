import requests
from bs4 import BeautifulSoup
import pymysql


# #DB 연결
# conn = pymysql.connect(host="14.32.66.116", port=10003,
#                        user="sl", passwd="sl",
#                        db="test_recode", charset='utf8', autocommit=True)
# cur = conn.cursor()

url = "http://www.wemakeprice.com/search/get_deal_more"

pageList = ['0', '30', '60', '90', '120', '150', '180', '210', '240', '270', '300', '330']

for page in pageList:
    res = requests.post(url,{"curr_deal_cnt": page,
                             "search_cate":'top',
                             '_service':5,
                             '_type':3,
                             'query_type':0,
                             'search_keyword':'1인용',
                             'r_cnt':30

                             })
    # print(res.json())
    html = BeautifulSoup(res.json()['html'])
    # print(html)
    prodLists = html.findAll("li")
    # print(lis)
    for prodList in prodLists:
        link = "http://www.wemakeprice.com"
        link += str(prodList).split('href="')[1].split('"')[0]
        print("link : " + link)

        title = str(prodList).split('"tit_desc">')[1].split('</strong>')[0]
        title = title.replace('amp;', '')
        print("title : " + title)

        img = str(prodList).split('original="')[1].split('"')[0]
        print("img : " + img)

        price = str(prodList).split('"sale">')[1].split('<')[0]
        print("price : " + price)

#         sql = "insert into sl_prodInfo (title, price, link, img) VALUES (%s, %s, %s, %s)"
#
#         cur.execute(sql, (title, pricee, link, img))
#
# conn.commit()
# cur.close()
# conn.close()
