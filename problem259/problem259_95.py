from collections import deque
import sys

N, u, v = map(int, input().split())
u -= 1; v -= 1
edge = [[] for _ in range(N)]
for s in sys.stdin.readlines():
    A, B = map(lambda x: int(x) - 1, s.split())
    edge[A].append(B)
    edge[B].append(A)

INF = float('inf')

# Aoki
pathV = [INF] * N
pathV[v] = 0
q = deque()
q.append((v, 0))
while q:
    p, d = q.popleft()
    nd = d + 1
    for np in edge[p]:
        if pathV[np] > nd:
            pathV[np] = nd
            q.append((np, nd))

# Takahashi
ans = 0
pathU = [INF] * N
pathU[u] = 0
q = deque()
q.append((u, 0))
while q:
    p, d = q.popleft()
    nd = d + 1
    if len(edge[p]) == 1:
        ans = max(ans, pathV[p] - 1)
    for np in edge[p]:
        if pathU[np] > nd and pathV[np] > nd:
            pathU[np] = nd
            q.append((np, nd))

print(ans)
