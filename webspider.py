import requests  #导入requests库
url="https://movie.douban.com/top250"  #指定url网址
headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36 Edg/81.0.416.53",
}   #指定headers信息，表示通过浏览器访问，可以反爬最简单一步
response=requests.get(url,headers=headers)    #请求访问目标网址，并得到一个response对象，包含text内容
response=response.text
print(response)

import re
from pprint import pprint

li_pattern=r"<li>(.*?)</li>"
lis=re.findall(
    pattern=li_pattern,
    string=response,
    flags=re.MULTILINE | re.DOTALL
)
pprint(lis)