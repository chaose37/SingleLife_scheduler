import pymysql
import requests
from bs4 import BeautifulSoup

# #DB 연결
conn = pymysql.connect(host="14.32.66.116", port=10003,
                       user="sl", passwd="sl",
                       db="test_recode", charset='utf8', autocommit=True)
cur = conn.cursor()

pageNo = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

for no in pageNo:
    res = requests.get("http://search.daum.net/search?q=%EA%B5%AD%EB%82%B4+%ED%98%BC%EC%9E%90+%EC%97%AC%ED%96%89%EA%B0%80%EA%B8%B0+%EC%A2%8B%EC%9D%80%EA%B3%B3&w=blog&m=&f=section&SA=daumsec&lpp=10&nil_profile=vsearch&nil_src=blog&page="+no+"&DA=PGD")
    soup = BeautifulSoup(res.content)

    travels = soup.findAll("ul", {"class", "list_info"})

    # print(travels)

    for travel in travels:
        lists = travel.findAll("li")
        for list in lists:
            if not list.find("a", {"class", "thumb"}):
                continue
            image = list.find("a", {"class", "thumb"})

            link = str(image).split('href="')[1].split('"')[0]
            img = str(image).split('src="')[1].split('"')[0]

            titles = list.find("a", {"class", "f_link_bu"})

            title = str(titles).split('_blank">')[1].split('</a>')[0]
            title = title.replace('<b>','')
            title = title.replace('</b>', '')

            dates = list.find("span", {"class", "date"})
            date = str(dates).split('>')[1].split('</')[0]

            print("img : " + img)
            print("link : " + link)
            print("title : " + title)
            print("date : " + date)
            sql = "insert into sl_travel(title, image, link, updatedate) values(%s, %s, %s, %s)"
            cur.execute(sql, (title, img, link, date))

conn.commit()
cur.close()
conn.close()