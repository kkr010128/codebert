#coding: UTF-8
N=int(input())
p=[int(input()) for i in range(0,N)]
maxv=p[1]-p[0]
buy=p[0]
for i in range(1,N):
    if p[i]-buy>maxv:
        maxv=p[i]-buy
    if p[i]<buy:
        buy=p[i]
print(maxv)