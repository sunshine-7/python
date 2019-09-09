
#计算文件中每个元素的个数
# f=open("raw.txt")

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

#简洁版
#计算文件中每个元素的个数
d = {}
f=open("raw.txt")
with open("raw.txt", "r") as f:
    for line in f:
         for j in line.strip().split(","):
            d[j] = d.get(j, 0) + 1
print(d)
