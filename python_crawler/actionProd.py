import requests
from bs4 import BeautifulSoup
import pymysql

# #DB 연결
# conn = pymysql.connect(host="14.32.66.116", port=10003,
#                        user="sl", passwd="sl",
#                        db="test_recode", charset='utf8', autocommit=True)
# cur = conn.cursor()

pageList = ['0', '1', '2', '3', '4', '5']

for page in pageList:
    res = requests.get("http://search.auction.co.kr/search/search.aspx?keyword=1%C0%CE%BB%F3%C7%B0&itemno=&nickname=&frm=hometab&dom=auction&isSuggestion=No&retry=&Fwk=1%C0%CE%BB%F3%C7%B0&acode=SRP_SU_0100&arraycategory=&encKeyword=1%25EC%259D%25B8%25EC%2583%2581%25ED%2592%2588&page="+page)
    soup = BeautifulSoup(res.content)

    auctionLists = soup.findAll("div", {"class", "list_view"})
    # print(auctionLists)

    for auctionList in auctionLists:
        # print(auctionList)
        title = str(auctionList).split('target="_blank">')[2].split('<')[0].strip()
        print("title : " + title)
        price = str(auctionList).split('strong>')[1].split('</')[0]
        print("price : " + price)
        img = str(auctionList).split('original="')[1].split('"')[0]
        print("img : " + img)
        link = "http://itempage3.auction.co.kr/DetailView.aspx?ItemNo="
        link += str(auctionList).split('ItemNo=')[1].split('"')[0]
        link.replace('amp','')
        print("link : " + link)

        # sql = "insert into sl_prodInfo (title, price, link, img) VALUES (%s, %s, %s, %s)"
        # cur.execute(sql, (title, pricee, link, img))

# conn.commit()
# cur.close()
# conn.close()



