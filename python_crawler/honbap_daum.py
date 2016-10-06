import requests
from bs4 import BeautifulSoup
import pymysql

# #DB 연결
# conn = pymysql.connect(host="14.32.66.116", port=10003,
#                        user="sl", passwd="sl",
#                        db="test_recode", charset='utf8', autocommit=True)
# cur = conn.cursor()

pageNo = ['1','2','3','4','5','6','7','8','9','10']

for no in pageNo:

    res = requests.get("http://search.daum.net/search?w=blog&nil_search=btn&enc=utf8&q=%ED%98%BC%EB%B0%A5+%EC%8B%9D%EB%8B%B9&page="+no+"&m=board&p=1&f=section&SA=tistory&DA=STC")
    soup = BeautifulSoup(res.content)


    honbaps = soup.findAll("ul",{"class":"list_info"})

    for honbap in honbaps:
         print('------------------------------------------')
         # print(honbap)
         print('------------------------------------------')
         bap = honbap.findAll("li")
         for b in bap:

             if b.find("div", {"class": "wrap_map"}):
                 if b.find("a",{"class":"thumb"}):
                     oriImage = b.find("a", {"class": "thumb"})
                     image = str(oriImage).split('src="')[1].split('"')[0]

                     oriTitle = b.find("a", {"class": "f_link_bu"})
                     title = str(oriTitle).split('target="_blank">')[1].split('</a>')[0]
                     title = title.replace('<b>', '')
                     title = title.replace('</b>', '')
                     oriLink = b.find("a", {"class" : "f_url"})
                     link = str(oriLink).split('href="')[1].split('"')[0]

                     oriDate = b.find("span",{"class":"date"})
                     date = str(oriDate).split('">')[1].split('</span>')[0]

                     print("------------------------------------------------")
                     print(image + "이미지요")
                     print(title + "제목요")
                     print(link + "링크요")
                     print(date + "날짜요")
                     r = requests.get(link)
                     s = BeautifulSoup(r.content)
                     print(link)
                     area = s
                     imgs = area.findAll("img")
                     count = 0
                     imgArr = []
                     for img in imgs :
                         if not str(img).__contains__("cfile"):
                             continue
                         if not str(img).__contains__("filename"):
                             continue
                         img = str(img).split('src="')[1].split('"')[0]
                         imgArr.append(img)
                         count+=1
                     print(imgArr)



#                      sql = "insert into sl_restaurant(title, image, link, regdate) values(%s, %s, %s, %s)"
#                      cur.execute(sql, (title, image, link, date))
# conn.commit()
# cur.close()
# conn.close()













