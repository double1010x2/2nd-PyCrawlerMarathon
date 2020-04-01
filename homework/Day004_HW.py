# %%
'''
# 利用 Python 存取 API


* 了解 Server Client 的架構與溝通方法
* 知道 HTTP Request & Response 的內容
* 什麼是 API？如何用 Python 程式存取 API 資料

'''

# %%
'''
## 作業目標

* 比較一下範例檔案中的「r.text」與「json.loads(r.text)」讀出來的內容有什麼差異
* 自行尋找一個合適的 API 接口做練習，並且查看其回傳內容
    * https://cat-fact.herokuapp.com/facts (來源：https://alexwohlbruck.github.io/cat-facts/)
    * http://odata.wra.gov.tw/v4/RealtimeWaterLevel (來源：https://data.gov.tw/dataset/25768)


'''

path1 = "https://cat-fact.herokuapp.com/facts"
path2 = "http://odata.wra.gov.tw/v4/RealtimeWaterLevel"
import requests
import json
r1 = requests.get(path1)
r2 = requests.get(path2)
rj1 = json.loads(r1.text)
rj2 = json.loads(r2.text)

# %%
'''
### 比較一下範例檔案中的「r.text」與「json.loads(r.text)」讀出來的內容有什麼差異
'''
print ("type of r1.text: ", type(r1.text))
print ("type of r2.text: ", type(r2.text))
print ("type of json.loads(r1.text): ", type(r1.text))
print ("type of json.loads(r2.text): ", type(r2.text))
# %%
path3 ="https://cat-fact.herokuapp.com/facts"
path4 ="http://odata.wra.gov.tw/v4/RealtimeWaterLevel"

data3 = json.loads(requests.get(path3).text)
data4 = json.loads(requests.get(path4).text)
print ("facts's keys: ", data3.keys())
print ("Keys of facts's 1st element: ", data3["all"][0].keys())
print ("waterLevel's keys: ", data4.keys())
# %%

# %%


# %%
