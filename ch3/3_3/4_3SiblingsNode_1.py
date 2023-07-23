from pyquery import PyQuery as pq

doc = pq(filename='demo1.html')
items = doc('.list .item-0.active')
siblings = items.siblings()
print(siblings)