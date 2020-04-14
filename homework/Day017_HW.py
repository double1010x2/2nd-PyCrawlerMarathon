# %%
'''
# HTTP 動態網頁架構說明


* 了解動態網頁的資料爬蟲策略
* 知道非同步網頁載入機制（Ajax）
* 學習兩種對應動態網頁爬蟲的的策略

'''

# %%
'''
## 作業目標

回答以下問題：

1. 動態網頁跟靜態網頁的差別是什麼？原本靜態網頁的做法會產生什麼問題或是缺點？
2. 還記得我們在 ETTODAY 靜態爬蟲實作練習中，有請大家完成一個題目「取出今天所有的發文」，但仔細看其實並沒有真的把當天所有的新聞都抓回來， 試著回答看看原因是什麼？及該如何檢查？

'''

# %%
'''
### 1. 動態網頁跟靜態網頁的差別是什麼？原本靜態網頁的做法會產生什麼問題或是缺點？
'''

# %
'''
Ans:
    (1) The response's return of dynamic webpages is an data or an API but a whole webpage when request a static webpage. Otherwise, one response by one request in static webpage, but dynamic webpages could request many times for some data.
    (2) The response's return of static webpage is large due to an whole webpages in return, but return of dynamic webpage after request could just be some data and easy handle on data analysis.

Reference for (2): http://www.j4.com.tw/customers-works/常聽到靜態網頁，動態網頁，如何分別？/
'''

# %%
'''
### 2. 還記得我們在 ETTODAY 靜態爬蟲實作練習中，有請大家完成一個題目「取出今天所有的發文」，但仔細看其實並沒有真的把當天所有的新聞都抓回來， 試著回答看看原因是什麼？及該如何檢查？
'''

# %%
'''
Ans: ETToday is a dynamic webpage, so only got one webpage in the response by beautifulSoup. However, the webpage would be change if you roll mouse wheel up and down and the move list would also change in one dynamic webpage. That's why no all news by beautifulSoup.
'''

# %%


# %%
