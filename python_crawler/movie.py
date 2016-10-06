import urllib.request
from bs4 import BeautifulSoup

url = "http://www.cgv.co.kr/movies/"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
html = response.read()

soup = BeautifulSoup(html)

#items = soup.findAll("div",{"class":"sect-movie-chart"})

#단일객체로 가져옴
content = soup.find("div",{"class":"sect-movie-chart"})

#리스트형태로 가져옴
#items = content.findAll("div",{"class":"box-contents"})
items = content.findAll("li")
urlArr = url.split("/")
rootUrl = ''

for index in range(3):
    rootUrl += urlArr[index]
    if index < 2:
        rootUrl+="/"


i=0
for item in items:
    if not str(item).__contains__("box-contents"):
        continue
    i+=1

    print(str(i)+"::::::")
    img = str(item.find("img")).split("\"")[5]
    print("img :::: "+img)


    title = str(item.findAll("strong",{"class":"title"})).split("<")
    print("제목 : "+title[1].split(">")[1])

    temp = item.findAll("strong",{"class":"percent"})

    percent = str(temp).split("<")
    print("예매율 : " + percent[2].split(">")[1])

    print("LINK : " + rootUrl + str(item.find("a")).split("\"")[1])

# 가져올 URL
#html = urllib.request.Request("http://movie.naver.com/movie/running/current.nhn?view=list&tab=normal&order=reserve")

#print(html.)

#soup = BeautifulSoup(html)
# 영화 제목이 페이지에 dt로 class 명이 tit로 되어 있기 때문이다.
# data = soup.findAll("dt", { "class" : "tit" })
# # 아래의 과정은 제목만 뽑아 내기 위함
# data = str(data)
# data = data.split("<")
# for i in range(len(data)):
#     if i % 5 == 2:
#         print (data[i].split(">")[1])