n=int(input())
A=list(map(int,input().split()))
mod=10**9+7

B=[[] for i in range(n)]
for i in range(n):
    B[i]= [((A[i]>>(59-j))) & 1 for j in range(60)]
    B[i] = [0]*(60-len(B[i]))+B[i]

TB=[[0]*n for i in range(60)]
for i in range(60):
    TB[i] = [B[j][i] for j in range(n)]
        
# import numpy as np
#print(TB)
ans=0
for i in range(60):
    now=TB[i]
    q=sum(now)
    
    ans+= ((pow(2,59-i,mod)* (q*(n-q)))%mod)%mod
    ans%=mod


print((ans)%mod)
    
     
