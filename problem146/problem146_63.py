import sys
input=sys.stdin.buffer.readline
mod=10**9+7
n=int(input())
d={}
z=0
from math import gcd 
for i in range(n):
    x,y=map(int,input().split())
    if x==y==0:z+=1
    else:
        f=gcd(x,y)
        x//=f;y//=f
        if x<0:x*=-1;y*=-1
        if x==0 and y<0:y=-y
        if (x,y)not in d:d[(x,y)]=1
        else:d[(x,y)]+=1
ans=1
for (a,s) in d:
    if d[(a,s)]==0:continue
    ng=0
    if (s,-a)in d:ng+=d[(s,-a)];d[(s,-a)]=0
    if (-s,a)in d:ng+=d[(-s,a)];d[(-s,a)]=0
    ans*=(pow(2,d[(a,s)],mod)-1 + pow(2,ng,mod)-1 +1)%mod
    ans%=mod
    d[(a,s)]=0
print((ans+z-1)%mod)