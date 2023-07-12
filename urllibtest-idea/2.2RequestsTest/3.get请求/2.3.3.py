import requests

r = requests.get('https://www.httpbin.org/get')
print(type(r.text))
print(r.json())
print(type(r.json()))