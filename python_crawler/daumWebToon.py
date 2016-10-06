import requests
import pymysql

conn = pymysql.connect(host="14.32.66.116", port=10003,
                       user="sl", passwd="sl",
                       db="test_recode", charset='utf8', autocommit=True)
cur = conn.cursor()

week = ['mon','tue','wed','thu','fri','sat','sun']
for day in week:
    url = "http://webtoon.daum.net/data/pc/webtoon/list_serialized/"+day
    res = requests.post(url)
    json = res.json()
    list = json['data']
    category='Webtoon'
    origin='daum'
    # print(list)
    for data in list:
        title = data['title']
        imgsrc = data['pcThumbnailImage']['url']
        writer = data['cartoon']['artists'][0]['name']
        link = "http://webtoon.daum.net/webtoon/view/"+data['nickname']
        ageGrade = data['ageGrade']
        print("*******************************************")
        print(title)
        print(link)
        print(imgsrc)
        print(writer)
        print(category)
        print(origin)
        print(day)
        star = 0;
        if ageGrade < 19:
            res = requests.post("http://webtoon.daum.net/data/pc/webtoon/view/"+data['nickname'])
            star = res.json()['data']['webtoon']['averageScore']
            star = round(star,2)

        print(star)



        sql = "insert into sl_play(title,image,link,category,writer,star,origin,updateday) " \
          " values(%s, %s, %s, %s, %s, %s, %s, %s) "
        cur.execute(sql, (title, imgsrc, link,category,writer,star,origin,day))

cur.close()
conn.close()


