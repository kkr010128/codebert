from math import gcd
from collections import defaultdict

n=int(input())
abd=defaultdict(int)
mod=10**9+7
wzero=0
azero=0
bzero=0
for i in range(n):
    a,b=map(int,input().split())
    if a==0 and b==0:
        wzero+=1
    elif a==0 and b!=0:
        azero+=1
    elif a!=0 and b==0:
        bzero+=1
    else:
        g=gcd(a,b)
        a=a//g
        b=b//g
        abd[(a,b)]+=1

liskey=list(abd.keys())
ans=1
for k in liskey:
    if abd[k] != 0:
        a,b=k
        x=abd[(a,b)]+abd[(-a,-b)]
        y=abd[(-b,a)]+abd[(b,-a)]
        abd[(a,b)]=0
        abd[(-a,-b)]=0
        abd[(-b,a)]=0
        abd[(b,-a)]=0
        ans*=(2**x+2**y-1+mod)%mod
        ans%=mod

ans*=(2**azero+2**bzero-1)
ans%=mod
ans=(ans+wzero)%mod
ans=(ans+mod-1)%mod
print(ans)