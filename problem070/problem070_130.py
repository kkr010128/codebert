from collections import deque
n, m = map(int ,input().split())
graph = [[] for _ in range(n)]
for i in range(m):
  a,b = map(int, input().split())
  graph[a-1].append(b-1)
  graph[b-1].append(a-1)
v = [0]*n
ans = 0
for i in range(n):
  if v[i] == 0:
    ans += 1
    q = deque()
    q.append(i)
    v[i] = 1
    while q:
      node = q.popleft()
      for j in graph[node]:
        if v[j] == 0:
          q.append(j)
          v[j] = 1
print(ans-1)