N, K = map(int, input().split())
MOD = 1000000007

fact = [0] * (N+1)
finv = [0] * len(fact)
inv  = [0] * len(fact)

fact[0] = fact[1] = 1
finv[0] = finv[1] = 1
inv[1] = 1
for i in range(2, len(fact)):
    fact[i] = fact[i-1] * i % MOD
#    inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
    inv[i] = - inv[MOD % i] * (MOD // i) % MOD
    finv[i] = finv[i - 1] * inv[i] % MOD

nCr = lambda n, r: fact[n] * finv[n-r] * finv[r] % MOD
nHr = lambda n, r: nCr(n+r-1, r)

# ans = 0
# for i in range(min(N-1, K) + 1):
#     ans += nCr(N, i) * nHr(N-i, i)
# ans = sum(nCr(N, i) * nHr(N-i, i) for i in range(min(N-1, K) + 1))
ans = sum(nCr(N, i) * nCr(N-1, i) for i in range(min(N-1, K) + 1))
print(ans % MOD)