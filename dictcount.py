f=open("raw.txt")
col=[]
dict = {}
list=[line.strip() for line in f]
for i in list:
    i=i.split(",")#走到这一步为什么一行一行地显示？？？
    col+=i
print(col)
for j in col:
    dict[j] = dict.get(j, 0) + 1
print(dict)
f.close()
