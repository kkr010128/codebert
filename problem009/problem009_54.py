from sys import stdin
from collections import deque

n = int(stdin.readline())
g = [None] * n
for _ in range(n):
    u, _, *cs = [int(s) for s in stdin.readline().split()]
    g[u-1] = [c - 1 for c in cs]
ds = [-1] * n
v = [False] * n
v[0] = True
q = deque([(0, 0)])
while len(q):
    u, d = q.popleft()
    ds[u] = d
    for c in g[u]:
        if not v[c]:
            v[c] = True
            q.append((c, d + 1))
for u, d in enumerate(ds):
    print(u + 1, d)