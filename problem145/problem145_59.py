from collections import deque

INF = 9999999

N, M = map(int, input().split())
to = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    to[a-1].append(b-1)
    to[b-1].append(a-1)

que = deque([0])
dist = [INF] * N
pre = [0] * N
dist[0] = 0
while que:
    from_v = que.popleft()
    for to_u in to[from_v]:
        if dist[to_u] != INF:
            continue
        dist[to_u] = dist[from_v]+1
        pre[to_u] = from_v
        que.append(to_u)

print('Yes')
for i in range(N):
    if i == 0:
        continue
    print(pre[i]+1)
