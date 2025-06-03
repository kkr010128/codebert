import sys
import  math
from heapq import *
import fractions
from collections import defaultdict
stdin = sys.stdin
     
ns = lambda: stdin.readline().rstrip()
ni = lambda: int(stdin.readline().rstrip())
nm = lambda: map(int, stdin.readline().split())
nl = lambda: list(map(int, stdin.readline().split()))

N=int(input())
A=nl()
A.sort(reverse=True)

mod=10**9+7
keta=[0]*60

for i in range(N):
    for j in range(60):    
        keta[j]+=((A[i]>>j)&1)

ans=0

mod_div2=[0]*60
mod_div2[0]=1
for i in range(1,60):
    mod_div2[i]=(2*mod_div2[i-1])%mod
    
for i in range(len(A)):
    keta_max=0
    for j in range(60):
        if((A[i]>>j)&1):
            keta_max=j+1
    for j in range(keta_max):
            if((A[i]>>j)&1):
                keta[j]-=1
                ans+=mod_div2[j]*(len(A)-i-1-keta[j])
            else:
                ans+=mod_div2[j]*keta[j]
            ans%=mod


print(ans%mod)