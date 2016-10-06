from bs4 import BeautifulSoup
import glob

files = glob.glob("c:/dev/test/*")

prodNum = 0;
for file in files:

    f = open(file,'r',encoding='utf-8')
    data = f.read()
    soup = BeautifulSoup(data)
    list = soup.find("ul")
    items = list.findAll("li")
    for item in items :
        if not str(item).__contains__("prodName"):
            continue
        name = item.findAll("p",{"class":"prodName"})
        print("상품명 : "+str(name))
        price = item.findAll("p",{"class":"prodPrice"})
        print("가격 : "+str(price))
        img = item.find("img")
        print("이미지 링크 : "+str(img))
        info = item.findAll("li")
        print("정보 : "+str(info))
        prodNum+=1
print(prodNum)
