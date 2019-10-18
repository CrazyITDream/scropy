import re
content = '''Hello 1234567  World This  
is a Regex Demo
'''
print(len(content))
result = re.match('^He.*?(\d+).*?Demo$', content, re.S)
print(result.group(1))

contents = '(百度)www.baidu.com'
results = re.match('\(百度\)www\.baidu\.com',contents)
print(results)











