import sys
import itertools
import numpy as np

MOD = 998244353
MAX = 10 ** 5 * 2 + 5

fac = [0 for i in range(MAX)]
finv = [0 for i in range(MAX)]
inv = [0 for i in range(MAX)]

def comInit(mod):
    fac[0], fac[1] = 1, 1
    finv[0], finv[1] = 1, 1
    inv[1] = 1
    for i in range(2, MAX):
        fac[i] = fac[i - 1] * i % mod
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        finv[i] = finv[i - 1] * inv[i] % mod

def com(n, r, mod):
    if n < r:
        return 0
    if n < 0 or r < 0:
        return 0
    return fac[n] * (finv[r] * finv[n - r] % mod) % mod

comInit(MOD)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
n, m, k = map(int, readline().split())

ans = 0
col = m
for x in range(n - 1, -1, -1):
    now = col
    now *= com(n - 1, x, MOD) % MOD
    if x <= k:
        ans += now
    col = (col * (m - 1)) % MOD

print(ans % MOD)