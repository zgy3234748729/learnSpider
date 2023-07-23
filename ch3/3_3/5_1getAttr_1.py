from pyquery import PyQuery as pq

doc = pq(filename='demo1.html')
a = doc('.list .item-0.active a')
print(a, type(a))
print(a.attr('href'))
print(a.attr.href)
