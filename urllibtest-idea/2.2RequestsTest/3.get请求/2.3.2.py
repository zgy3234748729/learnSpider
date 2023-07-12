import requests

data = {
    'name': 'germey',
    'age': 25
}
r = requests.get('https://www.httpbin.org/get', params=data)
print(r.text)