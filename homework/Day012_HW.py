# %%
'''
# Ettoday 網路爬蟲實作練習


* 能夠利用 Request + BeatifulSour 撰寫爬蟲，並存放到合適的資料結構

'''

# %%
'''
## 作業目標

根據範例 ，完成以下問題：

* ① 取出今天所有的發文
* ② 如果想要依照類別分類，怎麼儲存會比較好？
* ③ 哪一個類別的文章最多



'''
import requests
from bs4 import BeautifulSoup

url = 'https://www.ettoday.net/news/news-list.htm'
r = requests.get(url)

soup = BeautifulSoup(r.text, "html5lib")
class_dict = {}
title_all  = []
for d in soup.find(class_="part_list_2").find_all('h3'):
    ctype = d.find("em").get("class")[-1]
    title_all.append(d.find_all('a')[-1].text)
    if ctype in class_dict.keys():
        class_dict[ctype]["title"].append(d.find_all('a')[-1].text)
        class_dict[ctype]["date"].append(d.find(class_="date").text)
    else:
        class_dict[ctype] = {}
        class_dict[ctype]["title"] = []
        class_dict[ctype]["date"] = []

popular_class = ""
pcount  = -1
for di, dj in class_dict.items():
    if (len(dj["title"]) > pcount):
        popular_class = di
        pcount = len(dj["title"])
#print ("Most popular class: ", popular_class, ", count = ", pcount)
    #print(d.find(class_="date").text, d.find_all('a')[-1].text)
# %%
'''
### ① 取出今天所有的發文
'''

# %%
for ti in title_all:
    print ("Title: ", ti)
# %%
'''
### ② 如果想要依照類別分類，怎麼儲存會比較好？
'''

# %%
for di, dj in class_dict.items():
    print ("[%s]: \n" %di)
    for ti in dj["title"]:
        print ("\tTitle: %s" %(ti))
# %%
'''
### ③ 哪一個類別的文章最多
'''

# %%
print ("Most popular class: ", popular_class, ", count = ", pcount)
# %%


# %%


# %%
