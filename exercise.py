#将输入的str类型的数据转换成数值对象
def zh(str):     #不要用str str是内置的函数
    try:
        if type(eval(str))==int:
            str=int(str)
        elif type(eval(str))==float:
            str=float(str)
        return str
    except NameError as e:     #注意这里加了try except，因为如果输入不是数字就会报错
        return "请输数字 %s 不是数字" % str
#2-4
print("2-4题(a)显示用户输入的字符串"
      "     (b)将用户输入的数据转换成数值对象并显示")

def raw_input():       #不要和系统的函数名一样 ：< raw_input是系统函数
    #用户输入字符串，并输出
    string=input("请输入一个字符串：\n")
    print("您刚输入的字符串为：\n%s\n" %string,end="")
    #将用户输入数据转换成数值
    s = input("请输入一个数字，大小不限：\n")
    print("您刚输入的数字为：\n%s" % zh(s))
raw_input()



# 2-5(a)用while循环输出0到10
print("2-5分别用while和for循环输出0到10")
i=0
while i<=10:
    print(i,end=" ")
    i+=1
print("\r")
# 2-5(b)用for循环输出0到10
for i in range(0,11):
    print(i,end=" ")
print("\r")
# 2-6判断输入的数字正负
print("2-6判断输入的数字正负")
number=zh(input("请输入一个数字：\n"))
if number>0:
    print("您输入的是正数")
elif number<0:
    print("您输入的是负数")
else:
    print("您输入的是0")
# 2-7逐字符显示字符串
print("2-7分别用while和for循环逐字符显示字符串")
s=input("请输入一行字符串：\n")
i=0
#利用while循环逐字符遍历字符串①
#??????????
ite=iter(s)
while True:
    try:
        each = next(ite)
    except StopIteration:
        break
    print(each, end=" ")
print("\r")



#利用while循环逐字符遍历字符串②
while i<len(s):
    print(s[i],end=" ")
    i+=1
print("\r")
#利用for循环逐字符遍历字符串①
for i in s:
    print(i,end=" ")
print("\r")
#利用for循环逐字符遍历字符串②
for i in range(len(s)):
    print(s[i],end=" ")
print("\r")
#利用for循环逐字符遍历字符串③,带有索引
# for index, ch in enumerate(s):
#     print(index,end=' ')
#     print(ch)
#2-8对列表或元组中的元素求和
print("2-8分别用while和for循环对用户输入的数据求和")
# list1=[1,2,3,4,5]
# a=(1,2,3,4,5)
# print(sum(list1),sum(a),end="")
n=int(input(("请输入您要输入的数字个数：\n")))
i=1
li=[]
cal=0
#利用while循环求用户输入数字和
while i<=n:
    li.append(zh(input("请输入第%d个数:" %i)))
    i+=1
print("总和为：%f" %sum(li))
#利用for循环求用户输入数字和
for i in range(1,n+1):
    cal+=int(input("请输入第%d个数:" %i))
    i+=1
print("总和为：%f" %cal)
#2-15元素排序
#不能用列表，排序算法
print("2-15不能用列表，排序算法对3个元素进行排序")
n1=zh(input("请输入第一个数字："))
n2=zh(input("请输入第二个数字："))
n3=zh(input("请输入第三个数字："))
#从小到大排序
if n1>n2:
   n1,n2=n2,n1
if n2>n3:
  n2,n3=n3,n2
if n1>n2:
   n1,n2=n2,n1
print("从小到大排序：",end=" ")
print(n1,n2,n3)
#从大到小排序
if n1<n2:
   n1,n2=n2,n1
if n2<n3:
  n2,n3=n3,n2
if n1<n2:
   n1,n2=n2,n1
print("从大到小排序：",end=" ")
print(n1,n2,n3,end="")
#使用列表和冒泡排序
#n=int(input("请输入要求和的数字个数："))
# list2=[]
# for i in range(1,n+1):
#     list2.append(zh(input("请输入第%d个数:" %i)))
# print(list2)
# #从小到大
# for i in range(1,n):
#     for j in range(0,n-i):
#         if list2[j]>list2[j+1]:
#             list2[j], list2[j+1]=list2[j+1], list2[j]
# print(list2)
# #从大到小
# for i in range(1,n):
#     for j in range(0,n-i):
#         if list2[j]<list2[j+1]:
#             list2[j], list2[j+1]=list2[j+1], list2[j]
# print(list2)

