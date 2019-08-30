# print(dir([]))
# a = []
# a.append("fafsklk")
# print(a)
from functools import reduce
f=open(r"E:\PyCharmStart\t.txt","r")
string=[line.strip() for line in f if line.strip()=='bbb']
print(string)
#seek()移动文件读取指针移动到指定位置
f.seek(0)
number=[line.strip() for line in f if line.strip().isdigit()]
print(number)
f.seek(0)
#用int()方法输出整型
number=[int(line.rstrip()) for line in f if line.strip().isdigit()]
print(number)
#迭代器 iter， list列表是可迭代的，但不是迭代器，用iter()转换成迭代器
# it=iter(number)
#sum(),reduce()都是内置函数，不能prinr(sum)，要写print(sum(...))
print("10行数字求和为：",sum(number))
print("10行数字求和为：",reduce(lambda x, y: x+y, number))
f.close()
