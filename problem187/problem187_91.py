from collections import deque

N, X, Y = map(int, input().split())
adj = [[] for _ in range(N)]
for i in range(N-1):
    adj[i].append(i+1)
    adj[i+1].append(i)

adj[X-1].append(Y-1)
adj[Y-1].append(X-1)

dist = [[-1]*N for _ in range(N)]

for i in range(N):
    queue = deque([i])
    dist[i][i] = 0

    while queue:
        now = queue.popleft()
        for u in adj[now]:
            if dist[i][u] < 0:
                queue.append(u)
                dist[i][u] = dist[i][now] + 1

ans = [0] * (N-1)
for i in range(N):
    for j in range(i+1,N):
        ans[dist[i][j]-1] += 1

[print(a) for a in ans]