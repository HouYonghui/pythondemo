import requests  #导入requests库
url="https://movie.douban.com/top250"  #指定url网址
headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36 Edg/81.0.416.53",
}   #指定headers信息，表示通过浏览器访问，可以反爬最简单一步
response=requests.get(url,headers=headers)    #请求访问目标网址，并得到一个response对象，包含text内容
response=response.text    #获取text内容
print(response)

import re
from pprint import pprint  #引入pprint库，美化打印内容

li_pattern=r"<li>(.*?)</li>"   #按照正则表达式编写的匹配模式，网页标签并没有过多属性，因此只获取被“（）”包括的部分
lis=re.findall(
    pattern=li_pattern,
    string=response,
    flags=re.MULTILINE | re.DOTALL    #re.MULTILINE表示以换行符为间隔进行跨行匹配，re.DOTALL表示以.这个符号能够匹配到任意字符（包含空行空字符串），主要考虑到缩进的原因
)
pprint(lis)

titles = []
for node in lis:
    title = re.findall(
        pattern=r'<span class="(title|other)">(.*)</span>', 
        string=node
    ) #1
    title = [t[1].replace("&nbsp;", "").strip() for t in title] #2
    titles.append("".join(title)) #3

pprint(titles)



# -*- coding:utf-8 -*-
import requests

url = "https://movie.douban.com/top250"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36 Edg/81.0.416.53",
}

response = requests.get(url, headers=headers).text

from bs4 import BeautifulSoup

soup = BeautifulSoup(response)
print(soup)

lis = soup.select("ol.grid_view li")