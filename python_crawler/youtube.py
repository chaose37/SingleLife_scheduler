import requests
from bs4 import BeautifulSoup
import pymysql

def makeTag(url):
    url = url.split("&")[0]
    url = url.replace("watch?v=","embed/")

    tag = '<iframe id="YouTube_Player" width="560" height="315" src="' + str(url) + '" frameborder="0" allowfullscreen></iframe>'
    return tag

rootUrl = "https://www.youtube.com"
url = rootUrl+"/feed/trending"
res = requests.get(url).content.decode('utf-8')
soup = BeautifulSoup(res)
contents = soup.findAll("div",{"class":"yt-uix-tile"})
print(contents)
for content in contents :
    titleH3 = str(content.find("h3",{"class":"yt-lockup-title"}))

    link = rootUrl + titleH3.split('href="')[1].split('"')[0]
    if titleH3.__contains__("title='"):
        title = titleH3.split("title='")[1].split("'")[0]
    else:
        title = titleH3.split('title="')[1].split('"')[0]
    img = str(content.find("img"))
    if str(img).__contains__("data-thumb"):
        imgsrc = img.split('data-thumb="')[1].split('"')[0]
    else:
        imgsrc = img.split('src="')[1].split('"')[0]

    tag = makeTag(link)
    print(link)
    print(title)
    print(imgsrc)
    print(tag)
    print("=================================================")



