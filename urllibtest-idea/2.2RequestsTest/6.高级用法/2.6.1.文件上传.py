import requests

files = {'file': open('../3.get请求/favicon.ico', 'rb')}
r = requests.post('https://www.httpbin.org/post', files=files)
print(r.text)