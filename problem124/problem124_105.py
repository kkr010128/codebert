#!/usr/bin/env python3
import sys
input = sys.stdin.readline
MOD = 10**9 + 7
MAX_N = 2 * 10**6 + 10

# Construct factorial table
fac = [1] + [0] * MAX_N
for i in range(1, MAX_N+1):
    fac[i] = fac[i-1] * (i) % MOD

fac_inv = [1] + [0] * MAX_N
# Femrmat's little theorem says a**(p-1) mod p == 1
# then, a * a**(p-2) mod p == 1
# it means that a**(p-2) is the inverse element
# Here, Get 1 / n! first
fac_inv[MAX_N] = pow(fac[MAX_N], MOD-2, MOD)
for i in range(MAX_N, 1, -1):
    fac_inv[i-1] = fac_inv[i] * i % MOD

def mod_nCr(n, r):
    if n < r or n < 0 or r < 0:
        return 0
    tmp = fac_inv[n-r] * fac_inv[r] % MOD
    return tmp * fac[n] % MOD

k = int(input())
s = input().rstrip()
n = len(s)

ans = 0
for i in range(n, k + n + 1):
    ret = mod_nCr(i-1, n-1) * pow(25, i - n, MOD) * pow(26, k + n - i, MOD)
    ans += ret
    ans %= MOD
print(ans)