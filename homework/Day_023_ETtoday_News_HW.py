# %%
'''
# 東森新聞雲爬蟲練習
## 練習從東森新聞雲網站中，爬取新聞摘要及詳細內容。
## 學習利用Selenium模擬人為操作，更新動態網頁後爬取新聞內容。
'''

# %%
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# %%
'''
### 以財經新聞為例，先連結到財經新聞網頁，複製其URL。
'''

# %%
ETtoday_url = "https://www.ettoday.net/news/focus/%E8%B2%A1%E7%B6%93/"  #財經新聞

# %%
'''
### 用Selenium打開一個瀏覽器，連結到網站。然後模擬下拉網頁的動作，讓網頁完成更新，再處理後續動作。
'''

# %%
browser = webdriver.Chrome(executable_path='/Users/vincentwu/Documents/GitHub/2nd-PyCrawlerMarathon/homework/driver/chromedriver')
browser.get(ETtoday_url)  # 打開瀏覽器並連到東森新聞雲網頁

SCROLL_PAUSE_TIME = 1

#
# 以下是用Selenium模擬下拉網頁動作，讓網頁更新
#
last_height = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
while True:
    time.sleep(1)
    new_height = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    if new_height == last_height:
        break
    last_height = new_height
    '''
    提示：可參考以下的Stack Overflow:
    https://stackoverflow.com/questions/48850974/selenium-scroll-to-end-of-page-indynamically-loading-webpage/48851166
    '''

# %%
'''
### 到這裡網頁已經更新完畢，所有的新聞都已經出現在網頁上。接下來做爬取收集新聞的動作。
'''

# %%
#
# 這裡先建立一個函數，其功能是連到外部連結，並爬取新聞內容。
#
def getNewsDetailContent(link_url):
    resp = requests.get(link_url)
    resp.encoding = 'utf-8'
    #print(resp.text)

    soup = BeautifulSoup(resp.text, 'lxml')
    news_content = soup.find("div", attrs={'class':'story'}).find_all("p")
    for p in news_content:
        """
        .string屬性說明：
        (1) 若當前tag節點底下沒有其他tag子節點，會直接抓取內容(返回"NavigableString")
        (2) 若當前tag節點底下只有唯一的一個tag子節點，也會直接抓取tag子節點的內容(返回"NavigableString")
        (3) 但若當前tag節點底下還有很多個tag子節點，.string就無法判斷，(返回"None")
        """
        if ((p.string) is not None):
            print(p.string)

# %%
'''
### 解析HTML並萃取新聞摘要，若有外部的連結，再連到外部連結並把詳細新聞內容抓取下來。
'''
import pdb; pdb.set_trace()
# %%
# 爬取網頁內容，解析後萃取新聞摘要
html = browser.page_source
soup = BeautifulSoup(html, "lxml")
all_news = soup.find("div", attrs={'class':'block block_1 infinite_scroll'})

news_block = all_news.find_all('div', attrs={'class':'piece clearfix'})

for i, news_item in enumerate(news_block):
    print("----------------------------------------------------------------------")
    news_body = news_item.find('h3')
    print("\n[%d] %s\n" % (i, news_body.a.string))

    #
    # 連到外部連結，擷取詳細新聞內容
    #
    externalLink = "https://www.ettoday.net" + news_body.a["href"]
    getNewsDetailContent(externalLink)
