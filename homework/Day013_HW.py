# %%
'''
# PTT 網路爬蟲實作練習


* 能夠利用 Request + BeatifulSour 撰寫爬蟲，並存放到合適的資料結構

'''

# %%
'''
## PTT 網頁爬蟲
'''

# %%
import requests
from bs4 import BeautifulSoup

web_title = ["NBA", "coffee"]
for wi in web_title:
    url = 'https://www.ptt.cc/bbs/%s/index.html' %wi
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html5lib")
#    ff   = open("day013_data.txt", "w")
#    ff.write(r.text)
#    ff.close()
    ppt_dict = {}
    for di, d in enumerate(soup.find_all(class_="title")):
        #print(d.text.replace('\t', '').replace('\n', ''))
        title = d.text.replace('\t', '').replace('\n', '')
        if title in ppt_dict:
            continue
        else:
            ppt_dict[title] = {}
            ppt_dict[title]["date"]     = soup.find_all(class_="date")[di].text
            ppt_dict[title]["author"]   = soup.find_all(class_="author")[di].text
        try:
            r = BeautifulSoup(requests.get('https://www.ptt.cc'+d.find('a')['href']).text, "html5lib")
     #       print('作者: ' + r.find(class_='article-meta-value').text)
        except:
            continue

    import datetime
    last_title  = ""
    last_author = ""
    last_date   = ""
    last_date_op = datetime.datetime(2000,1,1)
    for di, dj in ppt_dict.items():
        date = dj["date"].split()[0].split("/")
        date = [int(dd) for dd in date]
        year = 2020 if date[0] <= 4 else 2019
        date = datetime.datetime(year, date[0], date[1])
        if date > last_date_op:
            last_title = di
            last_author = dj["author"]
            last_date   = dj["date"]
            last_date_op=date
    # %%
    '''
    ## 作業目標

    根據範例 ，完成以下問題：

    * ① 印出最新文章的「作者」「標題」「時間」
    * ② 印出第一頁所有文章的「作者」「標題」「時間」
    * ③ 試著爬爬看其他版的文章

    '''

    # < * ① 印出最新文章的「作者」「標題」「時間」>
    print ("Last Data of %s" %wi)
    print ("\tTitle: ", last_title)
    print ("\tAuthor: ", last_author)
    print ("\tdate: ",   last_date, "\n")


    # < * ② 印出第一頁所有文章的「作者」「標題」「時間」 >
    for di, dj in ppt_dict.items():
        print ("PPT %s" %wi)
        print ("\tTitle: ", di)
        print ("\tAuthor: ", dj["author"])
        print ("\tDate: ", dj["date"], "\n")

# < * ③ 試著爬爬看其他版的文章 >

