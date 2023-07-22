from pyquery import PyQuery as pq

doc = pq(filename='demo.html')
items = doc('.list')
lis = items.find('.active')
print(lis)