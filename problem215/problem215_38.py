n, k = map(int, input().split())
k = min(k, n - 1)

MOD = 1000000007

fact = [1] * (n + 1)
ifact = [0] * (n + 1)
for i in range(1, n + 1):
    fact[i] = fact[i - 1] * i % MOD
ifact[n] = pow(fact[n], MOD - 2, MOD)
for i in range(n, 0, -1):
    ifact[i - 1] = ifact[i] * i % MOD

def comb(n, k):
    if k < 0 or k > n:
        return 0
    return fact[n] * ifact[k] * ifact[n - k] % MOD

ans = 0
for i in range(k + 1):
    ans += comb(n, i) * comb(n - 1, i)
    ans %= MOD
print(ans)
