import sys

stdin = sys.stdin
inf = 1 << 60
mod = 1000000007

ni      = lambda: int(ns())
nin     = lambda y: [ni() for _ in range(y)]
na      = lambda: list(map(int, stdin.readline().split()))
nan     = lambda y: [na() for _ in range(y)]
nf      = lambda: float(ns())
nfn     = lambda y: [nf() for _ in range(y)]
nfa     = lambda: list(map(float, stdin.readline().split()))
nfan    = lambda y: [nfa() for _ in range(y)]
ns      = lambda: stdin.readline().rstrip()
nsn     = lambda y: [ns() for _ in range(y)]
ncl     = lambda y: [list(ns()) for _ in range(y)]
nas     = lambda: stdin.readline().split()

n, k = na()

def modpow(n, p, m):
    if p == 0:
        return 1
    if p % 2 == 0:
        t = modpow(n, p // 2, m)
        return t * t % m
    return n * modpow(n, p - 1, m) % m

d = [0] * (k + 1)

ans = 0
for i in range(k, 0, -1):
    d[i] = modpow(k // i, n, mod)
    j = 2
    while j * i <= k:
        d[i] -= d[j * i]
        j += 1
    ans += d[i] * i % mod

print(ans % mod)