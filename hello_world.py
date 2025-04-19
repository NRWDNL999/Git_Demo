from lxml import etree
# HTML 文件内容
html_content = '''
<html><body><div>
    <ul>
        <li><a href="link1.html">first item</a></li> 
        <li><a href="link2.html">second item</a></li> 
        <li><a href="link3.html">third item</a></li> 
        <li><a href="link4.html">fourth item</a></li> 
        <li><a href="link5.html">fifth item</a></li></ul>
</div></body></html>
'''
# 解析 HTML
tree = etree.HTML(html_content)

# (1) 查找所有名称为 <li> 的节点
li_nodes = tree.xpath('//li')
print("所有 <li> 节点：")
for node in li_nodes:
    print(etree.tostring(node, pretty_print=True).decode('utf-8'))

# (2) 查找 class 属性值为 item-0 的所有节点
item_0_nodes = tree.xpath('/*[@class="item-0"]')
print("\n所有 class='item-0' 的节点：")
for node in item_0_nodes:
    print(etree.tostring(node, pretty_print=True).decode('utf-8'))

# (3) 查找 <li> 下 href 属性值为 link1.html 的名称为 <a> 的子节点
a_nodes = tree.xpath('//li/a[@href="link1.html"]')
print("\n所有 <li> 下 href='link1.html' 的 <a> 子节点：")
for node in a_nodes:
    print(etree.tostring(node, pretty_print=True).decode('utf-8'))