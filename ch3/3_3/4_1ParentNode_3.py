from pyquery import PyQuery as pq

doc = pq(filename='demo1.html')
items = doc('.list')
print(items.parents('#container'))