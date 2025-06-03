from sys import stdin
mod = 10**9+7
N,K = [int(x) for x in stdin.readline().rstrip().split()]
A = [int(x) for x in stdin.readline().rstrip().split()]

maxn = 2*10**6

fac  = [0 for _ in range(maxn)]
finv = [0 for _ in range(maxn)]
inv  = [0 for _ in range(maxn)]

fac[0]  = fac[1] = 1
finv[0] = finv[1] = 1
inv[1] = 1

for i in range(2,maxn):
    fac[i] = fac[i-1] * i % mod
    inv[i] = mod - inv[mod%i] * (mod // i) % mod
    finv[i] = finv[i-1] * inv[i] % mod

def combinations(n,k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n-k] % mod) % mod

ans = 0
A.sort()
for ind,a in enumerate(A):
    ans -= a*combinations(N-ind-1,K-1) % mod
    ans %= mod
    
A.reverse()
for ind,a in enumerate(A):
    ans += a*combinations(N-ind-1,K-1) % mod
    ans %= mod
    
print(ans%mod)