# 输出所有小于等于n（n为大于2的正整数）的素数，每行10个素数
def prime(num):
    factor = 0
    for i in range(1,num+1):
        if num%i==0:
            factor+=1
    if factor==2:
        return num
    else:
        return "no"
def shuchu():
    flag=0
    n=int(input("请输入一个大于2的正整数\n"))
    while n<=2:
        n=input("数字需要大于2")
    for i in range(2,n+1):
        receive=prime(i)
        if receive!="no":
            print(receive,end=" ")
            flag+=1
        if flag==10:
            print("\n",end="")
            flag=0
shuchu()