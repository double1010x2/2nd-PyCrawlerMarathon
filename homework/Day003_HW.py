# %%
'''
# Python 下載XML檔案與解析


* 了解 xml 檔案格式與內容
* 能夠利用套件存取 xml 格式的檔案

'''

# %%
'''
## 作業目標

* 比較一下範例檔案中的「File I/O」與「xmltodict」讀出來的內容有什麼差異

* 根據範例檔案的結果：
    1. 請問高雄市有多少地區有溫度資料？
    2. 請取出每一個地區所記錄的第一個時間點跟溫度
    3. 請取出第一個地區所記錄的每一個時間點跟溫度
'''

# %%
'''
### 比較一下範例檔案中的「File I/O」與「xmltodict」讀出來的內容有什麼差異

'''
import urllib.request
import zipfile
import xmltodict

res = "http://opendata.cwb.gov.tw/govdownload?dataid=F-D0047-093&authorizationkey=rdec-key-123-45678-011121314"
urllib.request.urlretrieve(res, "./Data/example.zip")
f = zipfile.ZipFile('./Data/example.zip')
f.extractall('./Data')

# file IO method
fh = open("./Data/64_72hr_CH.xml", "r")
xml = fh.read()
fh.close()

#print(xml)
# 存取檔案
with open('./Data/64_72hr_CH.xml') as fd:
    doc = dict(xmltodict.parse(fd.read()))
print ("Type of IO: ", type(xml))
print ("Type of xmltodict: ", type(doc))
'''
 1. 請問高雄市有多少地區有溫度資料？
'''
kao_city_dict = doc['cwbopendata']['dataset']['locations']["location"]
# number of location
print ("number of location in Kaohsiung: %d" %len(kao_city_dict))

'''
2. 請取出每一個地區所記錄的第一個時間點跟溫度
3. 請取出第一個地區所記錄的每一個時間點跟溫度
'''
weather_dict_time= {}
for wi in kao_city_dict:
    local = wi["locationName"]
    weather_dict_time[local] = {}
    weather_dict_time[local]["1st_time"] = wi["weatherElement"][0]["time"][0]["dataTime"]
    time_list = [tt["dataTime"] for tt in wi["weatherElement"][0]["time"]]
    weather_dict_time[local]["all_time"] = time_list


time_1st = []
time_all = []
for ki, kv in weather_dict_time.items():
    time_1st.append(kv["1st_time"])
    time_all.append(kv["all_time"])

print ("1st_time list: ", time_1st)
print ("all_time list: ", time_all)
