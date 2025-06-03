import sys
readline = sys.stdin.readline

N,X,Y = map(int,readline().split())
G = [[] for i in range(N)]

for i in range(N - 1):
  G[i].append(i + 1)
  G[i + 1].append(i)
  
G[X - 1].append(Y - 1)
G[Y - 1].append(X - 1)

ans = [0] * N

from collections import deque
for i in range(N):
  q = deque([])
  q.append([i, -1, 0])
  seen = set()
  while q:
    v, parent,cost = q.popleft()
    if v in seen:
      continue
    seen.add(v)
    ans[cost] += 1
    for child in G[v]:
      if child == parent:
        continue
      q.append([child, i, cost + 1])
      
for i in range(1, N):
  print(ans[i] // 2)
