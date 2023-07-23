from pyquery import PyQuery as pq

doc = pq(filename='demo1.html')
item = doc('.list .item-0.active')
siblings = item.siblings()
print(siblings)