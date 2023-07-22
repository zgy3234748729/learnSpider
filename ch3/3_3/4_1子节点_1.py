from pyquery import PyQuery as pq

doc = pq(filename='demo.html')
items = doc('.list')
print(type(items))
print(items)
lis = items.find('li')
print(type(lis))
print(lis)
