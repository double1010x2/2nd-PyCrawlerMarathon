# %%
'''
# 靜態網頁的資料爬蟲策略


* 了解靜態網頁的資料爬蟲策略
* 認識適用於靜態網頁爬蟲的相關套件工具：Request
* 認識適用於靜態網頁爬蟲的相關套件工具：BeatifulSoup
'''

# %%
'''
## 作業目標

利用 Request + BeatifulSoup 爬取下列兩個網站內容並解析：

1. Dcared 網址： https://www.dcard.tw/f
2. 知乎： https://www.zhihu.com/explore

並且回答下面問題：

1. Request 取回之後該怎麼取出資料，資料型態是什麼？
2. 為什麼要使用 BeatifulSoup 處理？處理後的型態是什麼？
3. 觀察一下知乎回來的資料好像有點怪怪的，該怎麼解決？
'''

# %%
'''
### 1. Dcard 網址： https://www.dcard.tw/f
'''

# %%
import requests
from bs4 import BeautifulSoup
import json


# %%
url = 'https://www.dcard.tw/f'
r = requests.get(url)
'''
Your Code Here
'''

r.encoding = 'utf-8'
print(r.text[0:3000])

# %%
print('Request 取回之後該怎麼取出資料，資料型態是什麼？ =>', type(r.text))
try:
    response = json.loads(r.text)
    print("Type of request after json => ", type(response))
except:
    print ("failure on string to dict by json")
    print ("please try to use BeautifulSoup")
soup = BeautifulSoup(r.text, "html5lib")
# %%
print('為什麼要使用 BeatifulSoup 處理？處理後的型態是什麼？ => ', type(soup))
print (soup)


# %%
'''
### 2. 知乎： https://www.zhihu.com/explore
'''

# %%
url = 'https://www.zhihu.com/explore'
r = requests.get(url)
r.encoding = 'utf-8'

print(r.text[0:600])

# %%
'''
### 3. 觀察一下知乎回來的資料好像有點怪怪的，該怎麼解決？
Ans: use headers
'''

# %%
url = 'https://www.zhihu.com/explore'

headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
r.encoding = 'utf-8'
print(r.text[0:600])

soup = BeautifulSoup(r.text, "html5lib")
print (soup)
# %%


# %%
