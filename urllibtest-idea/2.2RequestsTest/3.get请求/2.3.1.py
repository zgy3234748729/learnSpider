import requests

r = requests.get('https://www.httpbin.org/get')
print(r.text)