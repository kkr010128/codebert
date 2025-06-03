import math
N,K= map(int, input().split())
a=[0]*(K+1)
co=0
mod=(10**9+7)
for i in range(K,0,-1):

    b=K//i
    t=2*i
    m=0
    while t<=K:
        m=m+a[t]
        t+=i
    c=pow(b,N,mod)
    a[i]=c-m
    co+=(a[i]*i)%mod


print(co%mod)
