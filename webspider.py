import requests
url="https://movie.douban.com/top250"
headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36 Edg/81.0.416.53",
}
response=requests.get(url,headers=headers)
response=response.text
print(response)