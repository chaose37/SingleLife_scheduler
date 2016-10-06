import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pymysql

#DB 연결
conn = pymysql.connect(host="14.32.66.116", port=10003,
                       user="sl", passwd="sl",
                       db="test_recode", charset='utf8', autocommit=True)
cur = conn.cursor()
today = datetime.today().strftime('%Y-%m-%d')
print(today)

for i in range(30):
    start = (i * 10)-9
    SearchURL = "https://search.naver.com/search.naver?where=post&sm=tab_pge&query=" \
                "%ED%98%BC%EB%B0%A5%20%EC%8B%9D%EB%8B%B9&st=sim&date_option=0" \
                "&date_from=&date_to=&dup_remove=1&post_blogurl=&post_blogurl_without=&srchby=all&nso=&ie=utf8&start="+str(start)+""
    res = requests.get(SearchURL)
    con = BeautifulSoup(res.content)
    list = con.findAll("li", {"class": "sh_blog_top"})
    for honbap in list:
        if honbap.find("a", {"class": "map_opn"}):
            oriLink = honbap.find("a",{"class" : "url"})
            oriTitle = honbap.findAll("a",{"class" : "sh_blog_title"})
            regDate = honbap.find("dd",{"class" : "txt_inline"})
            # print(oriTitle)
            link = str(oriLink).split('href="')[1].split('"')[0]
            img = str(honbap).split('src="https://tv.pstatic.net/ugc?t=r80&amp;q=')[1].split('"')[0]
            date = str(regDate).split('<dd class="txt_inline">')[1].split('<div class="scial"')[0]
            if str(oriTitle).__contains__("title='"):
                title = str(oriTitle).split("title='")[1].split("'>")[0]
            else:
                title = str(oriTitle).split('title="')[1].split('"')[0]

            if link.__contains__("blog.naver.com"):
                rooturl = link.split('?')[0]
                logNo = link.split("logNo=")[1]
                url = rooturl + "/" + logNo

            else:
               url = link
            print("---------------------------------------------------------------------------")
            print("포스트 제목 : " + title)
            print("포스트 주소 : " + url)
            print("포스트 이미지 : " + img)
            print("포스트 날짜 : " + date)
            print("---------------------------------------------------------------------------")


            sql = "insert into sl_restaurant(title, image, link, regdate) values(%s, %s, %s, %s)"
            cur.execute(sql, (title, img, url, date))

conn.commit()
cur.close()
conn.close()
