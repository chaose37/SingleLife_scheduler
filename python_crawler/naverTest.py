import requests

header = {
    'Host':'openapi.naver.com',
    'User-Agent':'curl/7.43.0',
    'Accept':'*/*',
    'Content-Type':'application/xml',
    'X-Naver-Client-Id':'fBtGVEMM3ycaYvSBQfuJ',
    "X-Naver-Client-Secret":"y_Qgt7tyxs",
}
r = requests.get("https://openapi.naver.com/v1/search/blog.xml?query=%EB%A6%AC%EB%B7%B0&display=10&start=1&sort=sim",
                 header=header)
