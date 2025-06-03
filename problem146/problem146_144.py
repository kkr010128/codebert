n=int(input())
mod=1000000007
import math
ab=[]
n0=0
for i in range(n):
    a,b = map(int,input().split())
    if a==0 and b==0:
        n0+=1
        continue
    if b==0:
        ab.append( (1,0) )
    elif a==0:
        ab.append( (0,1) )
    else:
        gc = math.gcd(a,b)*b//abs(b)
        ab.append( (a//gc,b//gc) )
n_eff = n-n0

from collections import Counter
c=Counter(ab)

pairs =[]
for cc in c:
    n_dual = c[(-cc[1],cc[0])]
    if n_dual>0:
#         print(cc)
        pairs.append( (c[cc],n_dual) )

ans=1
for p in pairs:
    ans = ans*(pow(2,p[0],mod)+pow(2,p[1],mod)-1 ) %mod

amari = n_eff - sum(sum(p) for p in pairs)

ans=ans * pow(2,amari,mod) %mod 

ans=ans+n0-1
print(ans%mod)