from pyquery import PyQuery as pq
doc = pq(filename='demo.html')
for item in doc('#container .list li').items():
	print(item.text())
