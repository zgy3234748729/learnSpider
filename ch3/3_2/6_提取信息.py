from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dormouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> abd
<a href="http://example.com/tillie" class="sister" id="link3">Tillie </a>
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html, 'lxml')
print(soup.title.name)  # 获取名称
print(soup.p.attrs)  # 获取所有属性
print(soup.p.attrs['name'])  # 获取name属性
print(soup.p['name'])
print(soup.p['class'])

# 获取内容
print('第一个p节点的文本：')
print(soup.p.string)

# 嵌套选择
print("soup.head.title:")
print(soup.head.title)
print("type(soup.head.title):")
print(type(soup.head.title))
print("soup.head.title.string:")
print(soup.head.title.string)
