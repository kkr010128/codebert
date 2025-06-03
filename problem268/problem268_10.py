import sys

N=int(input())
A=list(map(int,input().split()))
M=10**9+7

G={k:0 for k in range(-1,max(A)+1)}
G[-1]=3

X=1
for a in A:
    X*=G[a-1]-G[a]
    X%=M
    G[a]+=1
print(X)
