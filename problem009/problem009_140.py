from collections import deque

n = int(input())
adj = [[] for _ in range(n)]

for i in range(n):
  u,k,*v = map(int, input().split())
  v = [w-1 for w in v]
  adj[u-1].extend(v)

queue = deque([0])
ans = [-1] * n
ans[0] = 0

while queue:
  now = queue.popleft()
  
  for u in adj[now]:
    if ans[u] < 0:# 未訪問
      ans[u] = ans[now] + 1
      queue.append(u)

for i in range(n):
  print(i+1,ans[i])
