#计算文件中每个元素的个数
f=open("raw.txt")
col=[]
dict = {}
list=[line.strip() for line in f]
for i in list:
    i=i.split(",")
    col+=i
print(col)
for j in col:
    dict[j] = dict.get(j, 0) + 1
print(dict)
f.close()
