# %%
'''
# API 資料串接 - 以 Dcard API 實作範例

* 了解 Dcard API 使用方式與回傳內容
* 撰寫程式存取 API 且解析 JSON 格式資料

'''
import requests
import json
import numpy as np
path = ['https://www.dcard.tw/_api/forums/pet/posts?popular=true', 'https://www.dcard.tw/_api/forums/pet/posts?popular=false']
for pi in path:
    r = requests.get(pi)
    response = r.text

    response

    # %%
    data = json.loads(response)

    # %%
    '''
    ## 作業目標

    * 請利用 API: https://www.dcard.tw/_api/forums/pet/posts?popular=true 回答下列問題：

    1. 這個 API 一次會回傳幾筆資料？每一筆資料包含哪些欄位？
    2. 取出每一筆資料的「標題」、「貼文時間」、「留言人數」、「按讚人數」
    3. 計算熱門/非熱門文章的「平均留言人數」與「平均按讚人數」
    '''

    # %%
    # 1. 這個 API 一次會回傳幾筆資料？每一筆資料包含哪些欄位？
    status = "popular" if "true" in pi else "not popular"
    print ("[%s]How much data is: " %status, len(data))
    print ("[%s]What columns in each data: : "%status, data[0].keys())

    # %%
    # 2. 取出每一筆資料的「標題」、「貼文時間」、「留言人數」、「按讚人數」
    title_key = "title"
    create_key= "createdAt"
    reply_key = "commentCount"
    like_key  = "likeCount"

    title_list  = []
    create_list = []
    reply_list  = []
    like_list   = []
    #with open("data.txt", "w") as fh:
    #    for di in range(len(data)):
    #        fh.write("----- Data %d -----\n" %di)
    #        for ki, kj in data[di].items():
    #            fh.write("[%s]: \t%s\n" %(ki, kj))
    #        fh.write("\n")
    for dd in data:
        title_list.append(dd[title_key])
        create_list.append(dd[create_key])
        reply_list.append(dd[reply_key])
        like_list.append(dd[like_key])
    '''
    Your Code
    '''
    # Title print
    for ti in range(len(title_list)):
        print ("[%s]\n<Title>: %s\n<Create Time>: %s\n<Reply count>: %d\n<Like Count>: %d\n" %(status,title_list[ti], create_list[ti], reply_list[ti], like_list[ti]))

    # %%
    # 3. 計算熱門/非熱門文章的「平均留言人數」與「平均按讚人數」

    print ("[%s] average reply count: %.2f" %(status, np.mean(reply_list)))
    print ("[%s] average like count: %.2f" %(status, np.mean(like_list)))

# %%


# %%
