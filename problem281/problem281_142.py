from math import factorial as F
def comInit(mx=510000, mod=pow(10,9)+7):
    fac = [0]*mx
    finv = [0]*mx
    inv = [0]*mx
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2,mx):
        fac[i] = fac[i-1]*i%mod
        inv[i] = mod - inv[mod%i]*(mod//i)%mod
        finv[i] = finv[i-1]*inv[i]%mod
    return fac, finv

def com(fac, finv, n, k):
    if n<k: return 0
    if (n<0 or k<0): return 0
    return fac[n] * (finv[k]*finv[n-k]%mod)%mod

x, y = map(int, input().split())
mod = pow(10,9)+7
if (x+y)%3!=0:
    print(0)
else:
    w = (2*y-x)//3
    h = (2*x-y)//3
    if w<0 or h<0:
        print(0)
    else:
        fac, finv = comInit(w+h+1)
        print(com(fac, finv, w+h,w))