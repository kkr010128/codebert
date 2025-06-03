from fractions import gcd
from collections import Counter
slope=Counter()
slope_zero=0
slope_inf=0
both_zero=0
n=int(input())
for _ in range(n):
    a,b=map(int,input().split())
    if a==0 and b==0:
        both_zero+=1
    else:
        if a==0:
            slope_zero+=1
        elif b==0:
            slope_inf+=1
        else:
            sign=(a//abs(a))*(b//abs(b))
            a=abs(a)
            b=abs(b)
            gc=gcd(a,b)
            a//=gc
            b//=gc
            if sign==1:
                slope[(a,b)]+=1
            else:
                slope[(-a,b)]+=1
ans=1
mod=10**9+7
for a,b in slope.keys():
    if slope[(a,b)]>0:
        aa=-b
        bb=a
        if bb<0:
            bb*=-1
            aa*=-1
        if slope[(aa,bb)]>0:
            ans*=(pow(2,slope[(a,b)],mod)+pow(2,slope[(aa,bb)],mod)-1+mod)%mod
            ans%=mod
            slope[(aa,bb)]=0
        else:
            ans*=(pow(2,slope[(a,b)],mod))%mod
            ans%=mod
ans*=(pow(2,slope_zero,mod)+pow(2,slope_inf,mod)-1+mod)%mod
ans%=mod
ans+=both_zero
if ans>=mod:
    ans%=mod
print((ans-1+mod)%mod)


