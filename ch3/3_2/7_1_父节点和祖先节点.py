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
        </p>
        <p class="story">...</p>
"""
soup = BeautifulSoup(html, 'lxml')
# 获取a的父节点
print("获取a的父节点:")
print(type(soup.a.parent))
print(soup.a.parent)

# 获取a的祖先节点，返回类型为生成器类型
print("获取a的所有祖先节点：")
print(type(soup.a.parents))
print(list(enumerate(soup.a.parents)))
