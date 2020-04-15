# %%
'''
# Ettoday 網路爬蟲實作練習


* 能夠利用 Request + BeatifulSour 撰寫爬蟲，並存放到合適的資料結構

'''

# %%
'''
## Ettoday 網頁爬蟲
'''

# %%
'''
### 先複習一下原本純靜態的爬法
'''

# %%
# 先複習一下原本純靜態的爬法

import requests
from bs4 import BeautifulSoup
import numpy as np
url = 'https://www.ettoday.net/news/news-list.htm'
#r = requests.get(url)
##ff = open("day021_data.txt", "w")
##ff.write(r.text)
##ff.close()
#soup = BeautifulSoup(r.text, "html5lib")
#move_list = []
#for d in soup.find(class_="part_list_2").find_all('h3'):
#    move_list.append(d.find_all('a')[-1].text)
#    #print(d.find(class_="date").text, d.find_all('a')[-1].text)
#print ("count of news in ettoday: ", len(move_list))

# %%
'''
### 從上面的結果來看，你會發現它只會抓到最近的資料。原因是因為資料是透過下滑的過程中，利用 JavaScript 動態載入的。因此，這邊我們必須利用 selenium 這樣的工具來輔助：
'''

# %%
# 打開瀏覽器

from selenium import webdriver
from bs4 import BeautifulSoup
import time
from datetime import datetime
browser = webdriver.Chrome(executable_path='/Users/vincentwu/Documents/GitHub/2nd-PyCrawlerMarathon/homework/driver/chromedriver')

ettoday_dict = {"today": "https://www.ettoday.net/news/news-list.htm",
                "3days": "https://www.ettoday.net/news/news-list-2020-4-12-0.htm"
                }
for bi, bii in ettoday_dict.items():
    #browser.get("https://www.ettoday.net/news/news-list.htm")
    browser.get(bii)

    #for ei, ett in ettoday_dict.items():
    #    browser.get(ett)

    # %%
    # 每個兩秒鐘自動往下滑

    for i in range(10):
        time.sleep(2)
        browser.execute_script("window.scrollTo(0, 10000);")


    # %%
    # 取得資料，丟到 BeautifulSoup 解析

    html_source = browser.page_source
    soup = BeautifulSoup(html_source, "html5lib")
    move_list = []
    move_list_2hr = []
    current_hr= int(datetime.now().strftime("%H"))
    for d in soup.find(class_="part_list_2").find_all('h3'):
        news_title = d.find_all('a')[-1].text
        news_time  = d.find_all("span")[0].text.split("/")
        news_y     = int(news_time[0])
        news_m     = int(news_time[1])
        news_d     = int(news_time[2].split()[0])
        news_h     = int(news_time[2].split()[-1].split(":")[0])
        news_min   = int(news_time[2].split()[-1].split(":")[1])
        move_list.append(d.find_all('a')[-1].text)
        if (news_h <= current_hr)and(np.abs(news_h-current_hr)<= 2):
            move_list_2hr.append(news_title)
            #print(d.find(class_="date").text, d.find_all('a')[-1].text)


    # %%
    # 關閉瀏覽器
    #browser.quit();
    print ("[%s]"%(bi))
    print ("count of news in ettoday: ", len(move_list))
    print ("count of news in 2hours: ", len(move_list_2hr))
browser.quit();
# %%
'''
## 作業目標

根據範例：

1. 取出今天所有的新聞
2. 取出現在時間兩小時內的新聞
3. 根據範例，取出三天前下午三點到五點的新聞
'''

# %%
