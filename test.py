print("Hello!你好！")
import requests
response=requests.get('https://www.baidu.com')
print(response.content)