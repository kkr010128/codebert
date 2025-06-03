# -*- coding: utf-8 -*-

N,K=map(int,input().split())

MOD=998244353
D=[0]*(N+1)
D[1]=1

S=dict()
B=dict()
for i in range(K):
    L,R=map(int,input().split())
    S[i]=(L,R)
    B[i]=0


for i in range(2,N+1):
    for j in range(K):
        L,R=S[j][0],S[j][1]
        if i-L>0: B[j]+=D[i-L]
        if i-R-1>0: B[j]-=D[i-R-1]

        D[i]+=B[j]
        
    D[i]%=998244353

print(D[N])