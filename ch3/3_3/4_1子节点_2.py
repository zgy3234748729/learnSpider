from pyquery import PyQuery as pq

doc = pq(filename='demo.html')
items = doc('.list')
lis = items.children()
print(type(lis))
print(lis)