N, M, K = map(int, input().split())
MOD = 998244353

n = N
fac = [1]*(n+1)
rev = [1]*(n+1)
 
for i in range(1,n+1):
  fac[i] = i*fac[i-1]%MOD
  rev[i] = pow(fac[i], MOD-2, MOD)
 
comb = lambda a,b:(fac[a]*rev[a-b]*rev[b])%MOD
ans = 0

for i in range(K+1):
    ans += comb(N-1, N-1-i) * M * pow(M-1, N-1-i, MOD)
    ans %= MOD

print(ans)
