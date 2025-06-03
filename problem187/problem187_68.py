from collections import deque
 
N, X, Y = map(int, input().split())
ans = [0 for i in range(N)]

dqs = [-1, 1]
for i in range(N-1):
  vis = [-1 for _ in range(N)]
  Q = deque([i])
  vis[i] = 0
  while Q:
    q = Q.popleft()
    for dq in dqs:
      if 0 <= q + dq < N:
      	if vis[q + dq] == -1:
          vis[q + dq] = vis[q] + 1
          Q.append(q + dq)
          if q + dq > i:
            ans[vis[q + dq]] += 1
    if q==X-1:
      if vis[Y-1] == -1:
        vis[Y-1] = vis[q] + 1
        Q.append(Y-1)
        if Y-1 > i:
          ans[vis[Y-1]] += 1
    if q==Y-1:
      if vis[X-1] == -1:
        vis[X-1] = vis[q] + 1
        Q.append(X-1)
        if X-1 > i:
          ans[vis[X-1]] += 1
for a in ans[1:]:
  print(a)