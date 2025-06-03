import sys

stdin = sys.stdin
inf = 1 << 60
mod = 1000000007

sys.setrecursionlimit(10**7)

ni = lambda: int(ns())
nin = lambda y: [ni() for _ in range(y)]
na = lambda: list(map(int, stdin.readline().split()))
nan = lambda y: [na() for _ in range(y)]
nf = lambda: float(ns())
nfn = lambda y: [nf() for _ in range(y)]
nfa = lambda: list(map(float, stdin.readline().split()))
nfan = lambda y: [nfa() for _ in range(y)]
ns = lambda: stdin.readline().rstrip()
nsn = lambda y: [ns() for _ in range(y)]
ncl = lambda y: [list(ns()) for _ in range(y)]
nas = lambda: stdin.readline().split()

def modpow(n, p, m):
    if p == 0:
        return 1
    if p % 2 == 0:
        t = modpow(n, p // 2, m)
        return t * t % m
    return n * modpow(n, p - 1, m) % m

n = ni()

A = modpow(9, n, mod)
B = A
C = modpow(8, n, mod)
D = modpow(10, n, mod)

ans = (D - A - B + C) % mod

print(ans)