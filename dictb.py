f=open("kv.txt")
list=[line.strip() for line in f]
col=[]
value1=[]
value2=[]
j=0
for i in list:
    i=i.split(":")
    # print(i)
    col+=i
len=int(len(col)/2)
for j in range(0,len):
    value1.append(col[2*j])
    value2.append(col[2*j+1])
d1= dict(zip(value1,value2))
print(d1)
f.close()