n, x, y = map(int, input().split())
graph = [[] for _ in range(n)]
 
for i in range(n):
  if i+1 < n:
    graph[i].append(i+1)
  if i-1 >=0:
    graph[i].append(i-1)
graph[x-1].append(y-1)
graph[y-1].append(x-1)
 
ans = [0] * (n-1)
from collections import deque
for i in range(n):
  dist = [-1] * n
  dist[i] = 0
  d = deque()
  d.append(i)
  while d:
    v = d.popleft()
    for j in graph[v]:
      if dist[j] != -1:
        continue
      dist[j] = dist[v] + 1
      ans[dist[j] - 1] += 1
      d.append(j)
for a in ans:
  print(a//2)