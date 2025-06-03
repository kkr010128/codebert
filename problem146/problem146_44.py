import sys
input = sys.stdin.readline
import collections
import fractions
from collections import defaultdict
import math

n=int(input())
a= [list(map(int, input().split())) for i in range(n)]
b=defaultdict(int)
c=defaultdict(int)
b0=0
c0=0
mod=1000000007
ans=1
cnt=0
for i,j in a:
    if i!=0 and j!=0:
        x=i
        y=j
        i //= math.gcd(x, y)
        j //= math.gcd(x, y)
        i=abs(i)
        j=abs(j)
        if x*y>0:
            b[(i,j,0)]+=1
            c[(j,i,1)]+=1
        else:
            b[(i,j,1)]+=1
            c[(j,i,0)]+=1

    elif i==0 and j!=0:
        b0+=1
    elif i!=0 and j==0:
        c0+=1
    else:
        cnt+=1
w=[]
if c0!=0 or b0!=0:
    ans*=pow(2,c0+b0)-((pow(2,c0,mod)-1)*(pow(2,b0,mod)-1))

for k,v in b.items():
    if c[k]!=0:
        ans*=(pow(2,c[k]+v,mod)-(pow(2,c[k],mod)-1)*(pow(2,v,mod)-1))
        w.append((pow(2,c[k]+v,mod)-(pow(2,c[k],mod)-1)*(pow(2,v,mod)-1)))
        ans%=mod
    else:
        ans*=pow(2,v,mod)
        ans%=mod

w=collections.Counter(w)
w=list(w.most_common())
for i,j in w:
    for k in range(j//2):
        ans*=pow(i,mod-2,mod)
ans+=cnt-1
print(int(ans%mod))