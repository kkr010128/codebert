# -*- codinf: utf-8 -*-
from collections import deque

N, M = map(int, input().split())
route = [[] for _ in range(N + 1)]

for _ in range(M):
  a, b = map(int, input().split())
  route[a].append(b)
  route[b].append(a)
  
q = deque([1]) # 頂点を設定して初期化
pre = [None] * (N+1) # 頂点までの最短に進む時の次の頂点のリスト
pre[1] = 0 # 頂点は0
depth = [None] * (N+1) # 頂点からの深さ(最短距離)のリスト
depth[1] = 0 # 頂点の距離は0
while len(q) > 0:
  x = q.popleft()
  for r in route[x]:
    if pre[r] is None:
      depth[r] = depth[x] + 1
      pre[r] = x
      q.append(r)

print("Yes")
for i in range(2, len(pre)):
  print(pre[i])