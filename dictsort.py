###############################
##
## 这个做的不对，应到是先计算每一行的权重
## 然后排序的
##
###############################
kvDict = {}
with open("kv.txt", "r") as f2:
    for i in f2:
        i = i.strip().split(":")
        key, value = i[0], float(i[1])
        kvDict[key] = value

lineWithWeight = []
with open("raw.txt", "r") as f1:
    for line in f1:
        eles = line.strip().split(",")
        tw = sum([kvDict.get(e, 0) for e in eles])
        lineWithWeight.append((line, tw))
lineWithWeight.sort(key=lambda x: x[1])

with open("dictsort.txt","w") as f2:
    outputStr = "".join(map(lambda x: x[0].strip()+":"+str(x[1])+"\n", lineWithWeight))
    f2.write(outputStr)


# #对文件中每一行元素的权重和进行排序
# import numpy as np
# #打开全部都是元素的raw文件
# f1=open("raw.txt")
# #将raw文件中所有元素通过列表col1表示
# col1=[]
# #将raw文件中元素的名称以及个数通过字典d表示
# d={}
# raw=[]
# #以列表形式遍历raw文件每一行
# list1=[line1.strip() for line1 in f1]
# #遍历raw文件中的每一行的每一列
# for i in list1:
#     # 以“，”为分割符，将字符串分开
#     i = i.split(",")
#     # 将raw文件中分割好的每一行以列表的形式追加在一起，形成一个内含列表的列表，这个是追加列表
#     raw.append(i)
#     # 将raw文件中分割好的每一行以元素的形式追加在一起，存放在col1列表中，这个是追加元素
#     col1 += i
# for j in col1:
#     #将raw文件中的元素以及对应的元素个数存放在字典中
#     # d=dict.get(j, 0)会报错收到了一个str对象，而不是dict对象
#     #dict.get(j, 0)意思即如果字典d中存在j元素，则返回相对应的键值，否则就返回0，
#     # 所以这应该算是返回一个字符串，如果直接将其赋值给d,d是字典，会报错
#     #字典d的键为raw文件中的每个元素，键值为每个元素的个数
#     if d.has_key(j):
#         d[j] = d[j] + 1
#     else:
#         d[j] = 1
#     d[j] = d.get(j, 0) + 1
# print("raw每个元素个数：")
# print(d)
# f1.close()
# f2=open("kv.txt")
# #将kv文件中每一行以列表的形式表示
# list2=[line2.strip() for line2 in f2]
# #将kv文件中每个元素存放在col2列表中
# col2=[]
# #value1[]中存放kv文件中的所有元素
# #value2[]中存放kv文件中的所有权值
# value1=[]
# value2=[]
# j=0
# #遍历kv文件中的每一行，分割开以“：”为分割符的字符串
# for i in list2:
#     i=i.split(":")
#     #将kv文件中以元素的形式追加到col2列表中
#     col2+=i
# kvlen=int(len(col2)/2)
# for j in range(0,kvlen):
#     # value1[]中存放kv文件中的所有元素
#     # value2[]中存放kv文件中的所有权值
#     value1.append(col2[2*j])
#     value2.append(col2[2*j+1])
# #将kv文件中的元素以及对应的权值通过字典的形式表示
# d1=dict(zip(value1,value2))
# print("字典d1：")
# print(d1)
# f2.close()
# #将raw.txt文件中所有的键存放在列表v中
# # v=d.keys()
# n=0
# number=0
# cal=[]
# #遍历raw每一个元素
# for i in raw:
#     for j in i:
#         #判断raw中的元素在kv文件中是否存在
#          if j in d1:
#              number+=int(d1.get(j))
#     cal.append(number)
#     number=0  #一定记得给number重新赋值
# rawnum=range(1,int(len(list1))+1)
# #将每一行的权重放在字典d2中
# d2=dict(zip(rawnum,cal))
# print("raw文件每一行权重和为:")
# print(d2)
# print("raw文件权重总和为：")
# print(sum(cal))
# print("权重值经sorted排序后为：")
# print(sorted(cal))
# #权重排序后的索引
# index=np.argsort(cal)
# # print("权重排序后的索引为："  )
# # print(index)
# f2=open("dictsort.txt","w")
# for i in index:
#     f2.write(list1[i]+'\n')




