from lxml import etree

html = etree.parse('test.html', etree.HTMLParser())
# result = html.xpath('//li[@class="item-0"]/text()') # 因为li节点的直接子节点为a，没有文本内容。
result = html.xpath('//li[@class="item-0"]/a/text()') # 先选取特定的子孙节点，再调用text方法获取其内部文本
result = html.xpath('//li[@class="item-0"]//text()')  # 直接使用//加text方法，可以获取最全面的文本信息，但是会夹杂一些换行符等特殊字符
print(result)
