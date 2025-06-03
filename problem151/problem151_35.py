N, M, K = map(int,input().split())
MOD = 998244353

fac = [1 for i in range(N+1)]
for n in range(1,N+1):
    fac[n] = (n*fac[n-1])%MOD

fac_inv = [1 for i in range(n+1)]
fac_inv[N] = pow(fac[N],MOD-2,MOD)
for n in range(N-1,-1,-1):
    fac_inv[n] = (fac_inv[n+1]*(n+1))%MOD

def C(n,k):
    global MOD
    return (fac[n]*fac_inv[k]*fac_inv[n-k])%MOD

print(sum([C(N-1,b)*M*pow(M-1,N-1-b,MOD)%MOD for b in range(K+1)])%MOD)