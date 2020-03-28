# %%
'''
# Python 下載CSV檔案與解析


* 了解 csv 檔案格式與內容
* 能夠利用套件存取 csv 格式的檔案


'''

# %%
'''
## 作業目標

* 比較一下範例檔案中的「File I/O」與「CSV Reader」讀出來的內容有什麼差異

* 根據範例檔案的結果：
    1. 取出班次一的每一個時間
    2. 將班次一的每一個時間用一種資料型態保存
    3. 將班次一到五與其所有時間用一種資料型態個別保存

'''
import urllib.request
file_ex = "./Data/example.csv"
res = "http://opendata.hccg.gov.tw/dataset/432257df-491f-4875-8b56-dd814aee5d7b/resource/de014c8b-9b75-4152-9fc6-f0d499cefbe4/download/20150305140446074.csv"
urllib.request.urlretrieve(res, file_ex)

# File I/O method
line_io = []
with open(file_ex, "r") as fh:
    for fi in fh.readlines():
       line_io.append(fi)

# Read csv method
import csv
line_csv = []
# 開啟 CSV 檔案
with open(file_ex, newline='') as csvfile:
    # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)
    # 以迴圈輸出每一列
    for row in rows:
        line_csv.append(row)

# %%
'''
### 比較一下範例檔案中的「File I/O」與「CSV Reader」讀出來的內容有什麼差異

'''
# %%
print ("Line count different: File_IO(%d), CSV(%d)"%(len(line_io), len(line_csv)))
for l1, l2 in zip(line_io, line_csv):
    print ("count of each line different: File_IO(%d), CSV(%d)"%(len(l1), len(l2)))


# %%
'''
### 根據範例檔案的結果：

1. 取出班次一的每一個時間
2. 將班次一的每一個時間用一種資料型態保存
3. 將班次一到五與其所有時間用一種資料型態個別保存
'''

# %%
# 開啟 CSV 檔案
with open('./data/example.csv', newline='') as csvfile:
    # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)
    # 以迴圈輸出每一列
    for row in rows:
        print(row)
# %%
# 1. 取出班次一的每一個時間

import pandas as pd
data = pd.read_csv(file_ex)
key1 = data.columns[5]


# %%
# 2. 將班次一的每一個時間用一種資料型態保存
data[key1].to_csv(file_ex+".time1.csv")
with open(file_ex+".time1.2.csv", "w") as fh:
    fh.write(key1+"\n")
    for ff in data[key1]:
        fh.write(ff+"\n")

# %%
# 3. 將班次一到五與其所有時間用一種資料型態個別保存
key = data.columns[5:10]
data[key].to_csv(file_ex+".time1to5.csv")
with open(file_ex+".time1to5.2.csv", "w") as fh:
    for ki in key.tolist():
        fh.write(ki)
    fh.write("\n")
    for ff in data[key]:
        fh.write(ff+"\n")

# %%
