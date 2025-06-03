#coding:utf-8
n,m=list(map(int,input().split()))

A,b=[],[]
for i in range(n):
    A.append(list(map(int,input().split())))

for j in range(m):
    b.append(int(input()))

ans=[0 for i in range(n)]
for i in range(n):
    for j in range(m):
        ans[i]+=A[i][j]*b[j]

for i in ans:
    print(i)