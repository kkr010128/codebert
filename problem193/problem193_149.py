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

h, w, k = na()
s = nsn(h)

ans = inf
for bits in range(2 ** (h - 1)):
    binf = "{0:b}".format(bits)
    res = sum([int(b) for b in binf])
    divcnt = res + 1
    cnt = [0] * divcnt
    flag = True
    j = 0
    while j < w:
        cur = 0
        for i in range(h):
            if (s[i][j] == '1'):
                cnt[cur] += 1
            if bits >> i & 1:
                cur += 1
        if max(cnt) > k:
            if flag:
                res = inf
                break
            res += 1
            for i in range(divcnt):
                cnt[i] = 0
            flag = True
        else:
            flag = False
            j += 1
    ans = min(ans, res)

print(ans)