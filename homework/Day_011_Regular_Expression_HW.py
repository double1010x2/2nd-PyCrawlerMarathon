# %%
'''
# 正規表達式練習
## 在網路爬蟲當中，正規表達式常常用來過濾以及搜尋特定的pattern字串。
## 今天要來練習過濾IP address，以及URL。
'''

# %%
import re  #載入re模組

# %%
# 定義一個函數，用來測試是否能匹配正規表達式
def RegexMatchingTest(regex, input_text):
    #將正規表達式轉換成pattern
    pattern = re.compile(regex)

    # 使轉換後的pattern，來測試是否匹配
    result = re.search(pattern, input_text)

    if result:
        # 匹配完的結果會儲存在group()的屬性中，我們可以把匹配的結果列印出來
        print("Matched: %s" % (result.group()))

        if result.lastindex is not None:
            # group(0)代表整個字串，group(1)、group(2)...代表分組中，匹配的內容
            for i in range(0, result.lastindex+1):
                print("  group(%d): %s" % (i, result.group(i)))
    else:
        print("Not matched.")

# %%
'''
## 用正規表達式過濾IP address。
#### 一個合法的網路IP address，其格式為：X.X.X.X, 其中X是0~255的數字。我們可以用一個regex，來表達IP address的內容。
'''

# %%
test_string = "Google IP address is 216.58.200.227"

# 過濾IP address的regex pattern
regex = '(\d{1,3}).(\d{1,3}).(\d{1,3}).(\d{1,3})'
RegexMatchingTest(regex, test_string)

# %%
'''
#### 以上是最簡單的regex寫法。但深入思考，上面的regex也能夠匹配444.555.666.777這種無效的IP address。
#### 我們必須再雕琢regex，只接受[0~255].[0~255].[0~255].[0~255]這種合法的IP address，而過濾不合法的IP。
'''

# %%
'''
    Your code here.
    hint: 把IP可能出現的數字範圍，分開來思考
          1. 000 ~ 199
          2. 200 ~ 249
          3. 250 ~ 255
'''
#reference: https://www.regular-expressions.info/ip.html
regex = "(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[1-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[1-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[1-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[1-9])"

test_string1 = "Test IP 216.58.200.227"
RegexMatchingTest(regex, test_string1)  #測試表達式是否會匹配此合法IP

test_string2 = "Test IP 999.888.777.666"
RegexMatchingTest(regex, test_string2)  #測試表達式是否會匹配此不合法IP

# %%
'''
## 用正規表達式過濾URL。
#### 在網頁爬蟲中，常常會有外部連結的A tag，例如：
< a href="https://movies.yahoo.com.tw/movietime_result.html/id=9467"> 時刻表 < /a >
#### 我們要把"href="之後的URL擷取出來，用來做後續處理。
'''

# %%
html_a_tag = "<a href=https://movies.yahoo.com.tw/movietime_result.html/id=9467> 時刻表 </a>"

'''
    Your code here.
    過濾URL的regex pattern
'''
#reference from: https://stackoverflow.com/questions/10475027/extracting-url-link-using-regular-expression-re-string-matching-python
regex = 'https?://[^\s<>"]+|www\.[^\s<>"]+'
RegexMatchingTest(regex, html_a_tag)
