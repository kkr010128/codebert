from collections import deque


N, u, v = map(int, input().split())
u -= 1
v -= 1
edge = [[] for _ in range(N)]
for _ in range(N - 1):
    A, B = map(int, input().split())
    edge[A - 1].append(B - 1)
    edge[B - 1].append(A - 1)

INF = 10 ** 6
lenA = [INF] * N
q = deque()
q.append((v, 0))
lenA[v] = 0
while len(q) > 0:
    p, step = q.popleft()
    for np in edge[p]:
        if lenA[np] == INF:
            lenA[np] = step + 1
            q.append((np, step + 1))


lenT = [INF] * N
q = deque()
q.append((u, 0))
lenT[u] = 0
ans = 0
while len(q) > 0:
    p, step = q.popleft()
    if len(edge[p]) == 1:
        ans = max(ans, step + (lenA[p] - step) - 1)
    for np in edge[p]:
        if lenT[np] == INF and lenA[np] > step + 1:
            lenT[np] = step + 1
            q.append((np, step + 1))

print(ans)
