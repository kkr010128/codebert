N, M, K = map(int, input().split())
mod = 998244353

fact = [1 for i in range(N+1)]
fact_inv = [1 for i in range(N+1)]
for i in range(1, N+1):
    fact[i] = fact[i-1] * i %mod
    fact_inv[i] = pow(fact[i], mod-2, mod)

ans = 0
for k in range(K+1):
    x = M *pow(M-1, N-1-k, mod) *fact[N-1] *fact_inv[k] *fact_inv[N-1-k]
    ans += x %mod
    ans = ans %mod
print(ans)