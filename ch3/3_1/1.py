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
result = etree.tostring(html)   # etree模块可以自动修正HTML文本
print(result.decode('utf-8'))   # toString方法输入的结果是bytes类型，利用decode方法转成str类型

