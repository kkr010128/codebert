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

from collections import defaultdict

n, p = na()
s = ns()

if 10 % p == 0:
    ans = 0
    for i in range(n - 1, -1, -1):
        if int(s[i]) % p == 0:
            ans += i + 1
    print(ans)
    exit(0)

c = [0] * (n + 1)
m = 1
for i in range(n - 1, -1, -1):
    t = int(s[i]) * m % p
    c[i] = (c[i + 1] + t) % p
    m *= 10
    m %= p

ans = 0
dic = defaultdict(int)
for i in range(n, -1, -1):
    ans += dic[c[i]]
    dic[c[i]] += 1

print(ans)