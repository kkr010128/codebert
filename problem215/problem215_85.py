from collections import defaultdict


def mod_inv(a, m):
    return pow(a, m-2, m)


def combination(a, b):
    if b > a - b:
        return combination(a, a - b)
    ans = fact[a] * ifact[b] * ifact[a-b]
    return ans


MOD = 10**9+7
n, k = map(int, input().split())
k = min(k, n-1)

fact = defaultdict(int)
fact[0] = 1
for i in range(1, n+1):
    fact[i] = fact[i-1] * i
    fact[i] %= MOD

ifact = defaultdict(int)
ifact[n] = mod_inv(fact[n], MOD)
for i in reversed(range(1, n + 1)):
    ifact[i-1] = ifact[i] * i
    ifact[i-1] %= MOD

ans = 0
for i in range(k+1):
    ans += combination(n, i) * combination((n-i-1)+i, i)
    ans %= MOD

print(ans % MOD)
