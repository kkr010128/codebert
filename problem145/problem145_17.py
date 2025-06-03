from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dist = [[-1,0] for _ in range(n+1)]
dist[0][0] = 0
dist[1][0] = 0

d = deque()
d.append(1)

while d:
    v = d.popleft()
    for i in graph[v]:
        if dist[i][0] != -1:
            continue
        dist[i][0] = dist[v][0] + 1
        dist[i][1] = v
        d.append(i)

ans = dist[2:]

print('Yes')
for j in range(n-1):
    print(ans[j][1])