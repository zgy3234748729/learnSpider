from bs4 import BeautifulSoup

html = """
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>

        </ul>
    </div>
</div>
"""

soup = BeautifulSoup(html, 'lxml')

# 使用find_all方法，查询所有ul节点，返回结果为列表类型
print('调用find_all方法，查询所有ul节点：')
print(soup.find_all(name='ul'))
print(type(soup.find_all(name='ul')[0]))

# 使用嵌套查询，查询ul节点内部的li节点
print('查询ul节点内的li节点')
for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
    # 获取li节点内的内容
    for li in ul.find_all(name='li'):
        print(li.string)


# 根据属性查询
print('根据属性查询:')
print(soup.find_all(attrs={'id': 'list-1'}))
print(soup.find_all(attrs={'name': 'elements'}))

# 对于像id，class的属性，可以不用attrs传递
print('不使用attrs传递查询属性')
print(soup.find_all(id='list-1'))
print(soup.find_all(class_='element'))
