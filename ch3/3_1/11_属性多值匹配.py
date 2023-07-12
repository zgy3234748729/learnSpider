from lxml import etree

text = '''
<li class="li li-first"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
# result = html.xpath('//li[@class="li"]/a/text()') # li节点中class属性有两个值
result = html.xpath('//li[contains(@class, "li")]/a/text()')
print(result)
