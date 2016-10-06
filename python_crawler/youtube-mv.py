import requests
from bs4 import BeautifulSoup
import pymysql


def makeTag(url):
    url = url.split("&")[0]
    url = url.replace("watch?v=","embed/")

    tag = '<iframe id="YouTube_Player" width="560" height="315" src="' + str(url) + '" frameborder="0" allowfullscreen></iframe>'
    return tag


conn = pymysql.connect(host="14.32.66.116", port=10003,
                        user="sl", passwd="sl",
                        db="test_recode", charset='utf8', autocommit=True)
cur = conn.cursor()
playlists = [
            ['/playlist?list=PLiCvVJzBupKmPlfbRpTEf2o7V3St33QV8','game'],
            ['/playlist?list=PLFgquLnL59alGJcdc0BEZJb2p7IgkL0Oe','music'],
            ['/playlist?list=PL3ZQ5CpNulQmNiwTpPx8ABhh1Xeh38IWe','news'],
            ['/playlist?list=PLmtapKaZsgZt3g_uAPJbsMWdkVsznn_2R','popular']
            ]
for play in playlists :
    rootUrl = "https://www.youtube.com"
    url = rootUrl+play[0]
    res = requests.get(url).content.decode('utf-8')
    soup = BeautifulSoup(res,'lxml')
    table = soup.find("table",{"class":"pl-video-table"})
    contents = table.findAll("tr")
    for content in contents :
        img = str(content.find("img")).split('data-thumb="')[1].split('"')[0]
        titleTd = content.find("td",{"class":"pl-video-title"})
        title = str(titleTd.find("a"))
        link = rootUrl+title.split('href="')[1].split('"')[0]
        titleInner = title.split(">")[1].split("<")[0].strip()
        tag = makeTag(link)
        # info = BeautifulSoup(requests.get(link).content,'lxml')
        # writer = str(info.find("div",{"class":"yt-user-info"}).find("a")).split('>')[1].split("<")[0]
        category = play[1]
        print("===========================================")
        # print(writer)
        print("Link : "+link)
        print("Title : "+titleInner)
        print("Img : "+str(img))
        print("Tag : "+tag)


        sql = "insert into sl_play(title,image,link,category,tag,origin) " \
              " values(%s, %s, %s, %s, %s, %s) "
        cur.execute(sql,(titleInner,img,link,play[1],tag,"YouTube"))
cur.close()
conn.close()












