import requests
from bs4 import BeautifulSoup
from datetime import datetime

today = datetime.today().strftime('%Y-%m-%d')
print(today)

for i in range(30):
    SearchURL = "http://section.blog.naver.com/sub/SearchBlog.nhn?" \
                "type=post&option.keyword=국내혼자여행&term=period&option." \
                "startDate=" + "2016-07-01" + "&option.endDate=" + str(today) + "&" \
                "option.page.currentPage=" + str(i) + "" \
                                                                                                                      "&option.directoryAlias=domestic" \
                                                                                                                          "&option.orderBy=sim"
    # print(SearchURL)
    res = requests.get(SearchURL)
    con = BeautifulSoup(res.content)
    slist = con.find("ul", {"class": "search_list"})
    # print(slist)
    # list = slist.findAll("div",{"class":"list_data"})
    list = str(slist).split('search_list">')[1].split("</li>")
    for li in list:
        if not li.__contains__('input class="vBlogId"'):
            continue
        print("******************************")
        # print(li)
        id = li.split('class="vBlogId"')[1].split('value="')[1].split('"')[0]
        no = li.split('class="vLogNo"')[1].split('value="')[1].split('"')[0]
        print(id)
        print(no)
        oriURL = "http://blog.naver.com/PostView.nhn?blogId="+id+"&logNo="+no
        print(oriURL)
        data = li.split('class="list_data"')[1].split("</div>")[0]
        blogName = data.split(">")[2].split("<")[0]
        print(blogName)
        title = li.split("<h5>")[1].split('">')[1].split("</a>")[0]
        print(title)
        if data.__contains__("blog.naver.com"):
            rooturl = data.split('a href="')[1].split('"')[0]
            logNo = data.split("logNo=")[1].split("&")[0]
            url = rooturl + "/" + logNo
        else:
            url = li.split('a href="')[1].split('"')[0]

        print(url)
        r = requests.get(oriURL)
        s = BeautifulSoup(r.content)

        imgChk = 0
        img = "None"
        imgs = s.findAll("img")
        for i in imgs:
            if str(i).__contains__("http://postfile"):
                img = i
                imgChk=1
                break
        if imgChk :
            img = str(img).split('src="')[1].split('"')[0]

        print(img)





    # for li in list:
    #     # print(li)
    #     ft = str(li)
    #     if ft.__contains__("헬스") or ft.__contains__("헬스장") or ft.__contains__("건강"):
    #         continue
    #     elif ft.__contains__("병원") or ft.__contains__("피부관리") or ft.__contains__("다이어트") \
    #             or ft.__contains__("안과") or ft.__contains__("피부과") or ft.__contains__("성형외과"):
    #         continue
    #     elif ft.__contains__("아라시") or ft.__contains__("행사") or ft.__contains__("이벤트"):
    #         continue
    #     elif ft.__contains__("여행사") or ft.__contains__("리조트") or ft.__contains__("가이드"):
    #         continue
    #     elif ft.__contains__("유학") or ft.__contains__("로드") or ft.__contains__("웨이"):
    #         continue
    #     # elif ft.__contains__("해외") or ft.__contains__("대만") or ft.__contains__("일본") \
    #     #         or ft.__contains__("유럽") or ft.__contains__("미국") or ft.__contains__("중국") \
    #     #         or ft.__contains__("항공") or ft.__contains__("태국") or ft.__contains__("하와이") \
    #     #         or ft.__contains__("비행") or ft.__contains__("푸켓") or ft.__contains__("세부") \
    #     #         or ft.__contains__("동남아") or ft.__contains__("세부") or ft.__contains__("마카오"):
    #     #     continue
    #     elif ft.__contains__("뷰티") or ft.__contains__("교회") or ft.__contains__("판타지") \
    #             or ft.__contains__("하나님") or ft.__contains__("예수") or ft.__contains__("전생") \
    #             or ft.__contains__("위키") or ft.__contains__("월간") or ft.__contains__("고객") \
    #             or ft.__contains__("면세점") or ft.__contains__("박스오피스") :
    #         continue
    #
    #     # print(ft)
    #     title = str(li.find("h5").find("a")).split('">')[1].split("</a>")[0]
    #     data = li.find("div", {"class": "list_data"})
    #     date = str(data.find("span", {"class": "date"})).split(">")[1].split("<")[0]
    #     blogName = str(data).split(">")[2].split("<")[0]
    #     # print(data)
    #     if str(data).__contains__("blog.naver.com"):
    #         data = str(data)
    #         rooturl = data.split('a href="')[1].split('"')[0]
    #         logNo = data.split("logNo=")[1].split("&")[0]
    #         url = rooturl + "/" + logNo
    #     else:
    #         span = data.find("span", {"class": "category"})
    #         link = span.find("a")
    #         url = str(link).split('a href="')[1].split('"')[0]
    #
    #     # print(blogName)
    #     # print(date)
    #     # print(url)
    #     # print(title)
    #     # imgs = li.find("div",{"class":"multi_img"})
    #     r = requests.get(url)
    #     b = BeautifulSoup(r.content)
    #
    #     # print(b)
    #     print("////////")
