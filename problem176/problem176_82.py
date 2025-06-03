import sys
input = sys.stdin.readline
 
N,K=map(int,input().split())
mod=10**9+7
 
L=[i for i in range(K+1)]
 
for i in range(1,K):
    for j in range(i*2,K+1,i):
        L[j]-=L[i]
 
ANS=0
for i in range(1,K+1):
    ANS=(ANS+pow(K//i,N,mod)*L[i])%mod
 
print(ANS)