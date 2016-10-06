import pymysql
import requests

pageId = ['event/plus1','event/plus2','event/add','event/sale']
paramInfo =[1,2,3,4]


url = "http://minihomepage.cloudapp.net/MiniStopHomePage/page/querySimple.do"
imgPath = "http://minihomepage.cloudapp.net/MiniStopHomePage/page/pic.do?n=eventsale."
idx = 0
store = '7Eleven'

for idx in range(len(pageId)):
    i = 0
    while True:
        i+=1
        data = {'pageId':pageId[idx],'sqlnum':'1','paramInfo':str(paramInfo[idx])+'::',
                'pageNum':i}
        
        request = requests.post(url,params=data)
        j = request.json()
        l = j['recordList']
        if not l: break


        print("pageID :::"+pageId[idx])
        print(l)
        # DB와 연결
        conn = pymysql.connect(host="14.32.66.116", port=10003,
                               user="sl", passwd="sl", db="test_recode", charset='utf8', autocommit=True)
        cur = conn.cursor()
        for item in l :
            giftname = None
            giftimage = None
            prodName = None
            image = None
            price = None
            event = None
            fields = item['fields']
            if pageId[idx].__contains__("plus"):
                prodName = str(fields[0])
                price = str(fields[1])
                image = str(fields[4])
                if str(fields[2]) == '1':
                    event = '1+1'
                else :
                    event = '2+1'

            elif pageId[idx].__contains__("sale"):
                prodName = str(fields[1])
                price = str(fields[2])
                # print('sale_price : '+str(fields[3]))
                image = str(fields[5])
                event = "할인"
            else:
                prodName = str(fields[1])
                price = str(fields[2])
                giftname = str(fields[3])
                # print('event_price : '+str(fields[4]))
                image = str(fields[5])
                giftimage = str(fields[6])
                event = "증정"
            image = imgPath + image
            sql = " insert into sl_cvsinfo(prodname, price, event, image," \
                      "store, giftname, giftimage ) " \
                      " VALUES (%s, %s, %s, %s, %s, %s, %s ) "
            cur.execute(sql, (prodName,price,event,image,store,giftname,giftimage))

            conn.commit()

        cur.close()
        conn.close()

