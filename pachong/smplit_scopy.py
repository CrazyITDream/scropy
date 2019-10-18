'''
import urllib.request
import re
data = urllib.request.urlopen("https://read.douban.com/provider/all").read().decode("utf-8")
path = '<div class="name">(.*?)</div><div class="works-num">(.*?)</div>'
result = re.compile(path).findall(data)
f = open("name.txt", "w")
for i in range(len(result)):
    print(str(result[i][0]+"    "+result[i][1]))
    f.write(str(result[i][0]+"    "+result[i][1])+'\n')
f.close()


import urllib.request
import re
data = urllib.request.urlopen("https://read.douban.com/provider/all").read().decode("utf-8")
path = '<div class="works-num">(.*?)</div>|<div class="works-num">(.*?)</div>'
result = re.compile(path).findall(data)
print(result)


import urllib.request
for i in range(0, 4000):
    try:
        file = urllib.request.urlopen("http://192.21.100.7:8081/jwweb/MAINFRM.aspx", timeout=1)
        print(len(file.read().decode("gbk")))
    except Exception as err:
        print("出现异常"+str(err))

'''

import urllib.request, re

keyword = "python"
keyword = urllib.request.quote(keyword)
url = "http://www.baidu.com/s?wd="+keyword
data = urllib.request.urlopen(url).read().decode("utf-8")
path ="title:'(.*?)',"
res = re.compile(path).findall(data)
print(res)

















