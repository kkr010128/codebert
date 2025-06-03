n = int(input())
ab=[list(map(int,input().split())) for i in range(n)]
import math
from collections import defaultdict
d = defaultdict(int)
zerozero=0
azero=0
bzero=0
for tmp in ab:
    a,b=tmp

    if a==0 and b==0:
        zerozero+=1
        continue
    if a==0:
        azero+=1
        continue
    if b==0:
        bzero+=1
        continue

    absa=abs(a)
    absb=abs(b)
    gcd = math.gcd(absa,absb)

    absa//=gcd
    absb//=gcd

    if a*b >0:
        d[(absa,absb)]+=1
    else:
        d[(absa,-absb)]+=1

found = defaultdict(int)
d[(0,1)]=azero
d[(1,0)]=bzero

ans=1
mod=1000000007
for k in list(d.keys()):
    num = d[k]
    a,b=k

    if b>0:
        bad_ab = (b,-a)
    else:
        bad_ab = (-b,a)

    if found[k]!=0:
        continue
    found[bad_ab] = 1

    bm=d[bad_ab]

    if bm == 0:
        mul = pow(2,num,mod)
    if k==bad_ab:
        mul = num+1
    else:
        mul = pow(2,num,mod) + pow(2,bm,mod) -1
    ans*=mul

ans+=zerozero
ans-=1
print(ans%mod)