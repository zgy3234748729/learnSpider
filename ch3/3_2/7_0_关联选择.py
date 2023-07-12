from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""

soup = BeautifulSoup(html, 'lxml')
# 获取p的直接子节点(列表)
print("获取p的直接子节点(列表):")
print(soup.p.contents)

# 通过children来选择，返回结果为生成器类型
print("通过children来选择，返回结果为生成器类型:")
print(soup.p.children)
for i, child in enumerate(soup.p.children):
    print(i, child)

# 调用descendants属性，得到所有的子孙节点
print("调用descendants属性，得到所有的子孙节点：")
print(soup.p.descendants)
for i, child in enumerate(soup.p.descendants):
    print(i, child)

