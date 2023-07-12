import requests

r = requests.get('https://www.httpbin.org/get', timeout=(5, 30))
print(r.status_code)