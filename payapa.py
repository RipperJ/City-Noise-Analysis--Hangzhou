import requests
import os
import re
import http.cookiejar as cl
import time
from bs4 import BeautifulSoup as bs
#
f = open("results.txt", "a", encoding='utf-8')
#
def get_page(url, page_num):
    for i in range(1, page_num + 1):
        formdata = {
            "allContent":"噪音",
            "startTime":"2008-01-01",
            "endTime":"2020-01-01",
            "dataSort":"日期",
            "upOrDown":"降序",
            "cp":i,
            "lp":48
        }
        try:
            r = requests.get(url, data = formdata)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            print("OK!-link")
            print(r.text)
        except:
            print("EMM...link")
commonhead = "http://www.info0571.com/hbjtdb/"
page_url = "adv.html?allContentCondition=include&allContent=%E5%99%AA%E9%9F%B3%2C&searchType=like&contentCondition=include&content=&titleCondition=include&title=&authCondition=include&auth=&editorCondition=include&editor=&picauthCondition=include&picauth=&imageInfoCondition=include&imageInfo=&makeuperCondition=include&makeuper=&eyebrowHeadCondition=include&eyebrowHead=&subtitleCondition=include&subtitle=&serializeCondition=include&serialize=&topicCondition=include&topic=&timeCondition=include&startTime=2008-01-01&endTime=2020-01-01&editionCondition=include&edition=&editionNameCondition=include&editionName=&columnCondition=include&column=&paperChoose=&cp=~~~&lp=86"
headers = {
    'Cookie': "JSESSIONID=91296563285C692E9F4C6264DEED0F03; SESSION_LOGIN_USERNAME=82f923f4663e587d; SESSION_LOGIN_PASSWORD=82f923f4663e587d",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'Connection': 'Keep-Alive'
}
session = requests.Session()
count = 0
for i in range(1, 18):   # totally 86 pages
    print("It's page " + str(i) + " now.")
    res = session.get(commonhead + page_url.replace("~~~", str(i)), headers = headers)   # keep alive???
    html = res.text
    soup = bs(html, features="lxml")
    # print(soup.prettify())
    l = soup.find_all(href = re.compile("article.html"))
    # print(l)
    for j in l:
        # print(j)
        if (str(j).find("con_img") != -1):
            continue
        res_sub = session.get(commonhead + j.get('href'), headers = headers)
        html_sub = res_sub.text
        # print(html_sub)
        count += 1
        # print(count)
        soup_sub = bs(html_sub, features="lxml")
        title_sub = soup_sub.find("p", attrs = {"class": "maintitle"})
        article_sub = soup_sub.find("span", attrs = {"id": "articleContent"})
        # print(title_sub.get_text().strip())
        # print(article_sub.get_text().strip())
        f.write(title_sub.get_text().strip() + "\n")
        print(count, title_sub.get_text().strip())
        f.write(article_sub.get_text().strip() + "\n" + "\n")

f.close()
