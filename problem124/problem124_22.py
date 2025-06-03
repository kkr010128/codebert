K=int(input())
L=len(input())
from numba import*
@njit(cache=1)
def f():
    m=10**9+7
    max_n=2*10**6
    fac=[1]*(max_n+1)
    inv=[1]*(max_n+1)
    ifac=[1]*(max_n+1)
    for n in range(2,max_n+1):
        fac[n]=(fac[n-1]*n)%m
        inv[n]=m-inv[m%n]*(m//n)%m
        ifac[n]=(ifac[n-1]*inv[n])%m
    d=[1]*(K+1)
    d2=[1]*(K+1)
    for i in range(K):
        d[i+1]=d[i]*25%m
        d2[i+1]=d2[i]*26%m
    a=0
    for i in range(K+1):
        a=(a+fac[L+i-1]*ifac[i]%m*ifac[L-1]%m*d[i]%m*d2[K-i]%m)%m
    return a
print(f())