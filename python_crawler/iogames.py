import requests
from bs4 import BeautifulSoup
import pymysql

url = "https://www.reddit.com/r/IoGames/"
res = requests.get(url)
soup = BeautifulSoup(res.content)
games = soup.findAll("div",{"class":"thing"})
for game in games :
    img = game.find("img")

    if not img:
        imgsrc = "123"
    else:
        imgsrc = "http:" + str(game).split('src="')[1].split('"')[0]
    content = str(game.find("p",{"class":"title"}))
    link = content.split('href-url="')[1].split('"')[0]
    title = content.split('>')[2].split('<')[0]
    print(link)
    print(imgsrc)
    print(title)