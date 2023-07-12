import requests

# r = requests.get('https://www.httpbin.org/get')
# r = requests.post('https://www.httpbin.org/post')
# r = requests.put('https://www.httpbin.org/put')
r = requests.delete('https://www.httpbin.org/delete')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text[:100])
print(r.cookies)