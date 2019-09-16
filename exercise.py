#将输入的str类型的数据转换成数值对象
def zh(s):
    try:
        if type(eval(s))==int:
            s=int(s)
        elif type(eval(s))==float:
            s=float(s)
    except Exception:
        print("输入非数字")
        return "error"
    else:
        return s
#2-4
print("2-4题(a)显示用户输入的字符串"
      "     (b)将用户输入的数据转换成数值对象并显示")

def raw_input():       #不要和系统的函数名一样 ：< raw_input是系统函数
    #用户输入字符串，并输出
    s1=input("请输入一个字符串：\n")
    print("您刚输入的字符串为：\n%s\n" %s1,end="")
    #将用户输入数据转换成数值
    s2= input("请输入一个数字，大小不限：\n")
    while zh(s2) is "error":
        s2 = input("请输入一个数字：\n")
    print("您刚输入的数字为：\n%s" %zh(s2))
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
num=input("请输入一个数字：\n")
while zh(num) is "error":
    num = input("请输入一个数字：\n")
num=zh(num)
if num>0:
    print("您输入的是正数")
elif num<0:
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
n=input(("请输入您要输入的数字个数：\n"))
while zh(n) is "error":
    n = input("请输入一个数字：\n")
n=zh(n)
i=1
li=[]
cal=0
#利用while循环求用户输入数字和
while i<=n:
    num=input("请输入第%d个数:" %i)
    while zh(num) is "error":
        num=input("请输入数字，第%d个数:" %i)
    li.append(zh(num))
    i+=1
#如果依次输入-0.8  0.2  0.6 ，结果显示-0.000000？？？？？？？
if sum(li) == abs(sum(li)):
    print("总和为：%f" %abs(sum(li)))
else:
    print("总和为：%f" %sum(li))
#利用for循环求用户输入数字和
for i in range(1,n+1):
    num = input("请输入第%d个数:" % i)
    while zh(num) is "error":
        num = input("请输入数字，第%d个数:" % i)
    cal+=zh(num)
    i+=1
if cal == abs(cal):
    print("总和为：%f" %abs(cal))
else:
    print("总和为：%f" % cal)
#2-15元素排序
#不能用列表，排序算法
print("2-15不能用列表，排序算法对3个元素进行排序")
n1=input("请输入第一个数字：")
while zh(n1) is "error":
    n1 = input("请输入第一个数字：\n")
n2=input("请输入第二个数字：")
while zh(n2) is "error":
    n2 = input("请输入第二个数字：\n")
n3=input("请输入第三个数字：")
while zh(n3) is "error":
    n3 = input("请输入第三个数字：\n")
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
print(n1,n2,n3)
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

# # is 比较两个对象的 id 值是否相等，是否指向同一个内存地址；
# # 2、== 比较的是两个对象的内容是否相等，值是否相等；
# # 3、小整数对象[-5,256]在全局解释器范围内被放入缓存供重复使用；
# # 4、is 运算符比 == 效率高，在变量和None进行比较时，应该使用 is
# #4-1
a=10
b=10
c=100
d=100
e=10.0
f=10.0
print(a is b)
print(c is d)
print(e is f)
#6-1
import string
#判断字符串s2是否是s1的一部分
print("6-1判断小字符串是否包含在大字符串里")
s1=input("请输入一个大字符串：\n")
s2=input("请输入一个小字符串：\n")
if (s2 in s1) is True:
    print("小字符串是大字符串的一部分")
else:
    print("小字符串不是大字符串的一部分")
#去掉字符串的前后空格自定义函数
print("6-6通过自定义函数去除字符串的前后空格，不能使用.strip()")
def trim(s):
    if s[0]==" ":
        return trim(s[1:])
    if s[-1]==" ":
        return trim(s[:-1])
    else:
        return s
s3=input("请输入一个字符串：\n")
print(trim(s3))
#将字符串中大写换小写，小写换大写，自定义函数
#①
print("6-10将字符串中的大小写字母翻转")
def cap_change1(s):
    s1=""
    for i in range(0,len(s)):
        if s[i].isalpha():
            if s[i].isupper():
                s1+=s[i].lower()
            else:
                s1+= s[i].upper()
        else:
            s1+=s[i]
    return s1
# ②
def cap_change2(s):
    for i in s:
        if i.isalpha():
            if i.isupper():
                s=s.replace(i,i.lower())
            else:
                s=s.replace(i,i.upper())
    return s
#③
def cap_change3(s):
    s1=list(s)
    for i in range(0,len(s1)):
        if s1[i].isalpha():
            if s1[i].isupper():
                s1[i]=s1[i].lower()
            else:
                s1[i]=s1[i].upper()
    s="".join(s1)
    return s
s4=input("请输入一个字符串：\n")
print(cap_change1(s4)+"\n"+cap_change2(s4)+"\n"+cap_change3(s4))
import time
import datetime
class d:
    def caltime(self,date1,date2):
        try:
            date1=time.strptime(date1,"%m/%d/%Y")
            date2=time.strptime(date2,"%m/%d/%Y")
            date1=datetime.datetime(date1[0],date1[1],date1[2])
            date2=datetime.datetime(date2[0],date2[1],date2[2])
            return ((date2-date1).days)#将天数转成int型
        except Exception:
            print("输入格式不对")
            return "error"
obj=d()
# 计算两个日期之间相差的天数
print("6-15-1计算两个日期之间相差的天数，格式为月/日/年，xx/xx/xxxx")
dt1=input("请输入早日期:\n")
dt2=input("请输入晚日期:\n")
while obj.caltime(dt1,dt2) is "error":
    dt1 = input("请输入早日期，格式为月/日/年，xx/xx/xxxx:\n")
    dt2 = input("请输入晚日期，格式为月/日/年，xx/xx/xxxx:\n")
print("相差%s天" %obj.caltime(dt1,dt2))
# today=datetime.datetime.now().strptime()
# today=time.strptime()
# t=datetime.date.today()
#计算出生多少天
print("6-15-2计算出生多少天,格式为月/日/年，xx/xx/xxxx")
bir=input("请输入您的生日:\n")
t=""
t+=str(datetime.datetime.now().month)
t+="/"
t+=str(datetime.datetime.now().day)
t+="/"
t+=str(datetime.datetime.now().year)
print("今天日期为：%s" %t)
while obj.caltime(bir,t) is "error":
     bir=input("请输入您的生日；\n")
print("您已经来到这个世界%s天" %obj.caltime(bir,t))
print("6-15-3计算您还有多少天过生日")
bir=time.strptime(bir,"%m/%d/%Y")
if bir[1]<datetime.datetime.now().month:
    print("您还有%s天就过生日啦" %obj.caltime(t,str(bir[1])+"/"+str(bir[2])+"/"+str(datetime.datetime.now().year+1)))
else:
    print("您还有%s天就过生日啦" %obj.caltime(t,str(bir[1])+"/"+str(bir[2])+"/"+str(datetime.datetime.now().year)))
