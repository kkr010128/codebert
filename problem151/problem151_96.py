def COMinit():
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2,max):
        fac[i] = fac[i-1]*i%mod
        inv[i] = mod - inv[mod%i]*(mod//i)%mod
        finv[i] = finv[i-1]*inv[i]%mod

def COM(n,k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k]*finv[n-k]%mod)%mod

mod = 998244353
N,M,K = map(int,input().split())

max = max(N,2) 
fac = [0] * max
finv = [0] * max
inv = [0] * max
COMinit()
ans = 0
for i in range(K+1):
    c = COM(N-1,i)
    m = pow(M-1,N-i-1,mod)
    ans = (ans + ((c*m%mod)*M%mod))%mod
print(ans)
