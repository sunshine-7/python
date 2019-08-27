import urllib.request
file = urllib.request.urlopen("https://www.python.org")
html = file.read()
#price.textContent.trim()用来去掉静态网页中的空白
from lxml import etree
dom_tree = etree.HTML(html)
#如果相对路径中有双引号，路径用单引号括起来
con = []
for id in range(1,10):
    links = dom_tree.xpath('//*[@id="container"]/li[%s]/a'%id)
    parentTag = ""
    for i in links:
       parentTag = i.text
    print("^")
    tli = dom_tree.xpath('//*[@id="container"]/li[%s]/ul/li'%id)
    cList = []
    for id1 in range(1,len(tli)+1):
        links = dom_tree.xpath('//*[@id="container"]/li[%s]/ul/li[%s]/a' %(id,id1))
        for i in links:
            cList.append(i.text)
    if parentTag:     #python 真假值
        con.append(parentTag+"^" +":".join(cList))
result = "|".join(con)   #字符串 join
print(result)



