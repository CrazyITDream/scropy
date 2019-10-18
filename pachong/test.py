import re
import urllib.request
data = urllib.request.urlopen("https://read.douban.com/provider/63750322/").read().decode("utf-8")
path = '<a href="/ebook/56216122/">(.*?)</a>|<span class="orig-author">(.*?)</span>|<div class="rec-intro">(.*?)</div>|<span class="price-tag ">(.*?)</span>'
result = re.compile(path).findall(data)
for i in range(len(result)):
    print(result[i])




