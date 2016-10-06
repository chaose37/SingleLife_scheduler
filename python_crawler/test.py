import requests
from bs4 import BeautifulSoup
r = requests.get("http://blog.naver.com/PostView.nhn?blogId=kwoncase&logNo=220757705388")
c = r.content
s = BeautifulSoup(c)
imgs = s.findAll("img")
print(imgs)