from collections import deque

n, m = map(int, input().split())
nodes = range(1,n+1)
edges = {v: set() for v in nodes}
for _ in range(m):
  a, b = map(int, input().split())
  edges[a].add(b)
  edges[b].add(a)

visited = {v: False for v in nodes}
cnt = -1
for v in nodes:
  if not visited[v]:
    visited[v] = True
    que = deque([v])
    while que:
      p = que.popleft()
      for q in edges[p]:
        if not visited[q]:
          visited[q] = True
          que.append(q)
    cnt += 1
print(cnt)