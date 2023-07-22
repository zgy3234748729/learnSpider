from pyquery import PyQuery as pq
import requests

doc = pq(url='https://cuiqingcai.com')
print(doc('title'))

# 等同于一下代码
doc = pq(requests.get('https://cuiqingcai.com').text)
print(doc('title'))
