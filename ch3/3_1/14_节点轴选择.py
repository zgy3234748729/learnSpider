from lxml import etree

text = '''
<div>
    <ul>
        <li class="item-0"><a href="link1.html"><span>first iem</span></a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive"><a href="link3.html">third item</a></li>
        <li class="item-1"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a>
    </ul>
</div>
'''
html = etree.HTML(text)
result = html.xpath('//li[1]/ancestor::*')  # 返回第一个li节点的所有祖先节点
print(result)
result = html.xpath('//li[1]/ancestor::div')  # 增加div的限制条件
print(result)
result = html.xpath('//li[1]/attribute::*')  # 获取所有属性值
print(result)
result = html.xpath('//li[1]//child::a[@href="link1.html"]')  # 选取href属性为link1.html的
print(result)
result = html.xpath('//li[1]//descendant::span')
print(result)
result = html.xpath('//li[1]//following::*[2]')
print(result)
result = html.xpath('//li[1]//following::*')
print(result)
result = html.xpath('//li[1]//following-sibling::*')
print(result)
