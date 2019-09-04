# #计算文件中每个元素的个数
# f=open("raw.txt")
# #自定义的变量名最好不要与系统的保留字等一样， 比如下面的dict, list等
# #这里面很多中间变量都是可以去除的
# col=[]
# dict = {}
# list=[line.strip() for line in f]
# for i in list:
#     i=i.split(",")
#     col+=i
# print(col)
# for j in col:
#     dict[j] = dict.get(j, 0) + 1
# print(dict)
# f.close()


#########看一下下面一种实现##########
d = {}
with open("raw.txt", "r") as f:
    for line in f:
        for j in line.strip().split(","):
            d[j] = d.get(j, 0) + 1
print(d)
