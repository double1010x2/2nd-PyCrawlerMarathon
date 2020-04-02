# %%
'''
# API 資料串接 - 以 知乎 API 實作範例



* 了解知乎 API 使用方式與回傳內容
* 撰寫程式存取 API 且添加標頭



'''
import requests

# %%
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get('https://www.zhihu.com/api/v4/questions/55493026/answers',headers=headers)
response = r.text

# %%
import json
data = json.loads(response)

# %%
'''
## 作業目標

* 根據範例提供的 API ，完成以下問題：

    1. 取出知乎問題發問時間
    2. 取出第一筆與最後一筆回答的時間

'''
data_dict = {}
            #"question_time": {},
            # "question_title": {},
            # "1st_reply": {},
            # "last_reply": {}
            # }
for di in data["data"]:
    title = di["question"]["title"]
    if title in data_dict.keys():
        reply_time = di["created_time"]
        data_dict[title]["1st_reply"] = min(data_dict[title]["1st_reply"], reply_time)
        update_time = di["updated_time"]
        data_dict[title]["last_reply"] = max(data_dict[title]["last_reply"], update_time)
    else:
        data_dict[title] = {}
        data_dict[title]["question_time"] = di["question"]["created"]
        data_dict[title]["1st_reply"]     = di["created_time"]
        data_dict[title]["last_reply"]    = di["updated_time"]


# %%
'''
### 1. 取出知乎問題發問時間
'''
for di, dj in data_dict.items():
    print ("[%s]: question_time: %s" %(di, dj["question_time"]))
# %%
# 1. 取出知乎問題發問時間

'''
Your Code
'''

# %%
'''
### 2. 取出第一筆與最後一筆回答的時間
'''

# %%
# 2. 取出第一筆與最後一筆回答的時間
for di, dj in data_dict.items():
    print ("[%s]: 1st_reply: %s" %(di, dj["1st_reply"]))
    print ("[%s]: last_reply: %s\n" %(di, dj["last_reply"]))

'''
Your Code
'''

# %%


# %%


# %%
