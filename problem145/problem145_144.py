from collections import deque
n,m = map(int, input().split())
g = [[] for _ in range(n)]

for _ in range(m):
  a,b = map(int, input().split())
  a,b = a-1, b-1
  g[a].append(b)
  g[b].append(a)
stack = deque([0])
dist = [-1]*n
dist[0] = 0

while stack:
  v = stack.popleft()
  for nv in g[v]:
    if dist[nv] == -1:
      dist[nv] = v+1
      stack.append(nv)

print("Yes")
print(*dist[1:], sep= "\n")