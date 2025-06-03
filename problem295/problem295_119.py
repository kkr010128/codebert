import sys

stdin = sys.stdin
inf = 1 << 60
mod = 1000000007

sys.setrecursionlimit(10 ** 7)

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

def floyd_warshall(n, dist):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])


n, m, l = na()
abc = nan(m)
q = ni()
st = nan(q)

g = [[] for _ in range(n)]
dist = [[inf] * n for _ in range(n)]
for i in range(m):
    a, b, c = abc[i]
    a -= 1
    b -= 1
    dist[a][b] = c
    dist[b][a] = c

floyd_warshall(n, dist)

ans = [[inf] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if dist[i][j] <= l:
            ans[i][j] = 1
            ans[j][i] = 1

floyd_warshall(n, ans)

for i in range(q):
    s, t = st[i]
    s -= 1
    t -= 1
    if ans[s][t] >= inf:
        print(-1)
    else:
        print(ans[s][t] - 1)