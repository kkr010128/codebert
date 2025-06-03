from collections import deque
N, M = map(int, input().split())
Graph = [[]for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    Graph[a].append(b)
    Graph[b].append(a)

dist = [-1] * (N + 1)
dist[0] = 0
dist[1] = 0

pre = [-1] * (N + 1)
pre[0] = 0
pre[1] = 1

d = deque()
d.append(1)
while d:
    v = d.popleft()
    for i in Graph[v]:
        if dist[i] != -1:
            continue
        dist[i] = dist[v] + 1
        pre[i] = v
        d.append(i)
ans = dist[0:]
print('Yes')
for j in range(2, len(pre)):
    print(pre[j])
