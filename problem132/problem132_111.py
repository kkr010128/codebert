# 累積和で区間に操作ができる
import math
n,k=map(int,input().split())
A=list(map(int,input().split()))
kukan=[]
ans=[0]*n
for i in range(k):
    B=[0]*(n+1)#番兵は最後尾
    for j in range(n):
        l=max(0,j-A[j])
        r=min(j+A[j]+1,n)#右端の次の座標
        #print(l,r)
        B[l]+=1
        B[r]-=1
    for j in range(n):
        B[j+1]+=B[j]
    B.pop()#比較するために要素数を揃える
    if A==B:#飽和したら終わり
        break
    A=B#AにBをコピー
for b in B:
    print(b)