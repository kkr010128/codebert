#coding:utf-8
x=[[[0 for i in range(10)] for j in range(3)]for k in range(4)]

n=int(input())
for i in range(n):
    b,f,r,v=list(map(int,input().split()))

    x[b-1][f-1][r-1]+=v


for line,i in enumerate(x):
    for j in i:
        for k in j:
            print(" "+str(k),end="")
        print("")

    if line!=3:
        for i in range(20):
            print("#",end="")
        print("")