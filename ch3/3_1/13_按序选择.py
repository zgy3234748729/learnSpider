from lxml import etree

text = '''
<div>
    <ul>
        <li class="item-0"><a href="link1.html">first iem</a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive"><a href="link3.html">third item</a></li>
        <li class="item-1"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a>
    </ul>
</div>
'''
html = etree.HTML(text)
result = html.xpath('//li[1]/a/text()')             # 第一个li节点
print(result)
result = html.xpath('//li[last()]/a/text()')        # 最后一个li节点
print(result)
result = html.xpath('//li[position()<3]/a/text()')  # 前两个li节点
print(result)
result = html.xpath('//li[last()-2]/a/text()')      # 倒数第三个li节点
print(result)