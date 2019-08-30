#2019/8/20
#读txt文件，文件中有10行aaa，10行bbb,10行数字
#提取bbb,并求10行数字之和
#前面加r表示不做转义处理
#打开文件，返回一个文件对象
f=open(r"E:\PyCharmStart\t.txt","r")
number=0
#遍历文件
for line in f:
    #对每一行进行过滤，滤出想要的内容
    if line.strip()=='bbb':
        #end=""表示输出不换行
        print(line,end="")
    # 在windows下,txt文件中每一行会有一个不可见的分割符，
    # 即"\r\n"，所以line.isdigit()一直是false，如果最后一行是数字，那么只有最后一行是true。
    # 也就是说用line.isdigit()来判断，把不可见的"\r\n"也算进去啦
    # line.strip()是用来判断每一行具体内容的
    if line.strip().isdigit():
        number += int(line.strip())
f.close()
print(number, end="")
# Python中有三个去除头尾字符、空白符的函数，它们依次为:
# strip： 用来去除头尾字符、空白符(包括\n、\r、\t、' '，即：换行、回车、制表符、空格)
# lstrip：用来去除开头字符、空白符(包括\n、\r、\t、' '，即：换行、回车、制表符、空格)
# rstrip：用来去除结尾字符、空白符(包括\n、\r、\t、' '，即：换行、回车、制表符、空格)
# 这些函数都只会删除头和尾的字符，中间的不会删除。
# 用法分别为：
# string.strip([chars])
# string.lstrip([chars])
# string.rstrip([chars])
# string="I Love China!"
#字符串[:-n],取从第0个字符至倒数第n个字符的前一个字符
# print(string[:-3])