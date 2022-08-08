import requests
from bs4 import BeautifulSoup
import json
headers=json.loads({
    Accept: application/json, text/plain, */*
    Accept-Encoding: gzip, deflate, br
    Accept-Language: zh-CN,zh;q=0.9
    Connection: keep-alive
    Cookie: _itt=1; GCID=16fab22-8a5ee2a-d8aa9f5-4b90c5a; GCESS=BgEI8nYcAAAAAAAEBACNJwADBMh.vWIIAQMKBAAAAAACBMh.vWIFBAAAAAANAQEJAQELAgYABgQ63QtWBwSeGux6DAEB; _ga=GA1.2.1176977113.1656586042; GRID=16fab22-8a5ee2a-d8aa9f5-4b90c5a; ACTID=f2c18b38c5f2794fca36; LF_ID=1657270532584-4758690-7958830; Hm_lvt_094d2af1d9a57fd9249b3fa259428445=1656586042,1657270533; Hm_lpvt_094d2af1d9a57fd9249b3fa259428445=1657270533; _gid=GA1.2.1513279013.1657270533; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221865458%22%2C%22first_id%22%3A%22181b438f914b50-0bc15f1ba7f91d-50684254-1327104-181b438f915b78%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fwww.infoq.cn%2Fnews%2F%22%7D%2C%22%24device_id%22%3A%22181b438f914b50-0bc15f1ba7f91d-50684254-1327104-181b438f915b78%22%7D; SERVERID=3431a294a18c59fc8f5805662e2bd51e|1657270545|1657270532
    Host: www.infoq.cn
    Referer: https://www.infoq.cn/news/
    Sec-Fetch-Dest: empty
    Sec-Fetch-Mode: cors
    Sec-Fetch-Site: same-origin
    User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/30
})
print(headers)
# url='https://www.infoq.cn/news/'
# def craw2(url):
#     response1=requests.get(url,headers=headers)
#     soup=BeautifulSoup(response1,'lxml')
#     for title_href in soup.find_all('div',class='page-title')
#         print([title.get('title') for title in title_href.find_all('a') if title.get('title')])