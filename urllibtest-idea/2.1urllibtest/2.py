from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy_handler = ProxyHandler({
    'http': 'http://192.168.40.1:8080',
    'https': 'https://192.168.40.1:8080'
})
opener = build_opener(proxy_handler)
try:
    response = opener.open('https://www.csdn.com')
    print(response.read().deocde('utf-8'))
except URLError as e:
    print(e.reason)