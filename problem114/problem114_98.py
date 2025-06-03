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

d = ni()
c = na()
s = nan(d)
t = nin(d)

last = [0] * 26

ans = 0
for i in range(d):
    sa = s[i]
    cur = t[i]
    cur -= 1
    ans += sa[cur]
    last[cur] = (i + 1)
    for j in range(26):
        ans -= c[j] * ((i + 1) - last[j])
    print(ans)