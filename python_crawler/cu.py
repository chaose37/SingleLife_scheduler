import pymysql
import requests
from bs4 import BeautifulSoup


def insert_db(prod,eventitem):

    name = prod.find("p", {"class": "prodName"})
    price = prod.find("span")
    event = prod.find("li")
    photo = prod.find("img")

    pname = str(name).split(">")[2].split("<")[0]
    price = str(price).split(">")[1].split("<")[0]
    event = str(event).split(">")[1].split("<")[0]
    photo = str(photo).split("src")[1].split("\"")[1]

    # DB와 연결
    conn = pymysql.connect(host="14.32.66.116", port=10003,
                           user="sl", passwd="sl", db="test_recode", charset='utf8', autocommit=True)
    cur = conn.cursor()
    price = price.replace(',', '')
    if not eventitem:
        sql = " insert into sl_cvsinfo(prodname, price, event, image, store) " \
              " VALUES (%s, %s, %s, %s, %s) "
        cur.execute(sql, (pname.encode('utf8'), price.encode('utf8')
                      , event.encode('utf8'), photo.encode('utf8'), "CU".encode('utf8')))
    else :
        ename = eventitem.find("p", {"class": "prodName"})
        ephoto = eventitem.find("img")
        ename = str(ename).split(">")[2].split("<")[0]
        ephoto = str(ephoto).split("src")[1].split("\"")[1]

        sql = " insert into sl_cvsinfo(prodname, price, event, image," \
              "store, giftname, giftimage ) " \
              " VALUES (%s, %s, %s, %s, %s, %s, %s ) "
        cur.execute(sql, (pname.encode('utf8'), price.encode('utf8')
                          , event.encode('utf8'), photo.encode('utf8'), "CU".encode('utf8'),
                          ename.encode('utf8'),ephoto.encode('utf8')))
    conn.commit()

    cur.close()
    conn.close()

list = []
pageIndex = 1
while True :

    url = "http://cu.bgfretail.com/event/plusAjax.do"
    idx = 0
    data = {'pageIndex':pageIndex,'listType':'1','searchCoundition':''}
    pageIndex+=1
    request = requests.post(url,params=data)
    request.encoding = 'utf8'
    soup = BeautifulSoup(request.content)
    print('pageIndex :::::::: ' + str(pageIndex))

    if str(soup).__contains__("조회된 상품이 없습니다."):
        break

    items = soup.findAll("ul")
    for item in items:
        if not item.find("div"):
            continue
        list.append(item)
idx = 0

for page in list:

    prods = page.findAll("li")

    for prod in prods:
        if prod.find("p") == None:
            continue
        idx+=1
        event = None
        insert_db(prod,event)

url = "http://cu.bgfretail.com/event/presentAjax.do"
request = requests.get(url)
soup = BeautifulSoup(request.content)
list = soup.findAll("div",{"class":"presentListBox"})

for item in list :
    prod = item.find("div",{"class":"presentList-w"})
    event = item.find("div",{"class":"presentList-e"})
    insert_db(prod,event)