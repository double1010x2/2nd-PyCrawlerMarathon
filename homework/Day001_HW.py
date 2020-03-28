# %%
'''
# 資料來源與檔案存取

* 資料來源與取得
* 開放資料
* 資料儲存格式
* Python 存取檔案
'''

# %%
'''
## 作業目標

* 1.（簡答題）檔案、API、爬蟲三種取得資料方式有什麼不同？
* 2.（實作）完成一個程式，需滿足下列需求：
    * 下載指定檔案到 Data 資料夾，存成檔名 Homework.txt
    * 檢查 Data 資料夾是否有 Homework.txt 檔名之檔案
    * 將「Hello World」字串覆寫到 Homework.txt 檔案
    * 檢查 Homework.txt 檔案字數是否符合 Hello World 字數

'''

# %%
'''
### 1.（簡答題）檔案、API、爬蟲三種取得資料方式有什麼不同？
Ans:
資料的來來源⽅方式很多，檔案 & API 是由資料擁有者主動釋出，爬蟲則是資料擁 有者被動公開的。所以需要取得資料的時，通常會先考慮前兩兩者⽅方法，真的無 法才使⽤用網⾴頁爬蟲。
'''

# %%
'''
### 2.（實作）完成一個程式，需滿足下列需求：
    * 下載指定檔案到 Data 資料夾，存成檔名 Homework.txt
    * 檢查 Data 資料夾是否有 Homework.txt 檔名之檔案
    * 將「Hello World」字串覆寫到 Homework.txt 檔案
    * 檢查 Homework.txt 檔案字數是否符合 Hello World 字數

'''

# %%
# 根據需求引入正確的 Library

from urllib.request import urlretrieve
import os

# %%
# 下載檔案到 Data 資料夾，存成檔名 Homework.txt
homework = "Homework.txt"
path     = "./Data/"
try:
    os.makedirs( path, exist_ok=True )
    urlretrieve ("https://www.w3.org/TR/PNG/iso_8859-1.txt", path+homework)
except:
    print('發生錯誤！')

# %%
# 檢查 Data 資料夾是否有 Homework.txt 檔名之檔案

#files = []
files = os.listdir(path)


'''
Your Code
'''
if homework in files:
    print('[O] 檢查 Data 資料夾是否有 Homework.txt 檔名之檔案')
else:
    print('[X] 檢查 Data 資料夾是否有 Homework.txt 檔名之檔案')

# %%
# 將「Hello World」字串覆寫到 Homework.txt 檔案

f = ''

with open(path+homework, "w") as fh:
    fh.write("Hello World")

try:
    with open(path+homework, "r") as fh:
        f = fh.read()
except EnvironmentError: # parent of IOError, OSError *and* WindowsError where available
    pass



# %%
# 檢查 Homework.txt 檔案字數是否符合 Hello World 字數

if len('Hello World') == len(f):
    print('[O] 檢查 Homework.txt 檔案字數是否符合 Hello World 字數')
else:
    print('[X] 檢查 Homework.txt 檔案字數是否符合 Hello World 字數')

# %%


# %%


# %%
