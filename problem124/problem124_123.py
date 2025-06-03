
from collections import defaultdict

# ----------

INF = float("inf")
MOD = 10 ** 9 + 7
# ----------

def combination(a, b):
    if b > a - b:
        return combination(a, a - b)
    return fact[a] * ifact[b] * ifact[a-b]


K = int(input())
S = input().strip()
N = len(S)

# 階乗を前処理
fact = defaultdict(int)
fact[0] = 1
for i in range(1, N+K+1):
    fact[i] = fact[i-1] * i
    fact[i] %= MOD
# 階乗の逆元を前処理
ifact = defaultdict(int)
ifact[N+K] = pow(fact[N+K], MOD-2, MOD)
for i in reversed(range(1, N+K+1)):
    ifact[i-1] = ifact[i] * i
    ifact[i-1] %= MOD

ans = 0
for i in range(K+1):
    now = pow(26, K-i, MOD)
    now *= pow(25, i, MOD)
    now %= MOD
    now *= combination(i+N-1, N-1)
    now %= MOD
    ans += now
    ans %= MOD

print(ans)
