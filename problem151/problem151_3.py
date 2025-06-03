from functools import reduce

def cin():  return list(map(int,input().split()))
N, M, K = cin()
MOD = 998244353

fac = [1] * (N + 1)
inv = [1] * (N + 1)

for j in range(1, N + 1):  fac[j] = fac[j - 1] * j % MOD

inv[N] = pow(fac[N], MOD - 2, MOD)
for j in range(N - 1, -1, -1):  inv[j] = inv[j + 1] * (j + 1) % MOD
    
def cmb(n, r):
    if r > n or n < 0 or r < 0:  return 0
    return fac[n] * inv[n - r] * inv[r] % MOD

ans = 0
for i in range(K + 1):
    ans += M * cmb(N - 1, i) * pow(M - 1, N - 1 - i, MOD)
    ans %= MOD
print(ans)