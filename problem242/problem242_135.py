n,k = map(int,input().split())
a = [int(i) for i in input().split()]
a.sort()
mod = 10**9+7
fac = [0]*(n+1)
finv = [0]*(n+1)
def comb(n,k):
    if n < k: return 0
    if n < 0 or k < 0: return 0
    return fac[n]*finv[k]%mod*finv[n-k]%mod
fac[0] = finv[0] = 1
for i in range(1,n+1):
    fac[i] = fac[i-1]*i%mod
    finv[i] = pow(fac[i],mod-2,mod)
smin = 0
smax = 0
for i in range(n):
    smin += (a[i]*comb(n-i-1,k-1))%mod
    smin %= mod
    smax += (a[n-1-i]*comb(n-i-1,k-1))%mod
    smax %= mod
ans = (smax-smin)%mod
print(ans)