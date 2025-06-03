N,K=map(int,input().split())
A=list(map(int,input().split()))
m,p,z=[],[],0
for a in A:
    if a<0:
        m.append(a)
    elif a>0:
        p.append(a)
    else:
        z+=1
m.sort()
p.sort()
mod=10**9+7
from functools import reduce
if (len(p) or K%2==0) and K<len(m)+len(p) or K==len(m)+len(p) and len(m)%2==0:
    r=1
    i,j=0,0
    while i+j<K:
        if i<len(m)-1 and i+j<K-1 and (j>=len(p)-1 or m[i]*m[i+1]>p[-j-1]*p[-j-2]):
            r=r*m[i]*m[i+1]%mod
            i+=2
        else:
            r=r*p[-j-1]%mod
            j+=1
    print(r)
elif z:
    print(0)
else:
    print(reduce(lambda x,y:x*y%mod,(m+p)[-K:]))