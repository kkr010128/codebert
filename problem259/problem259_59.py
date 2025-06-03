N, u, v = map(int, input().split())
target = u-1
v -= 1
edge = [[] for _ in range(N)]
for i in range(N-1):
  a,b = map(int, input().split())
  edge[a-1].append(b-1)
  edge[b-1].append(a-1)

from collections import deque
def bfs(s):
  lis = [-1]*N
  d = deque([s])
  lis[s]=0
  while len(d)>0:
    v = d.popleft()
    for w in edge[v]:
      if lis[w]<0:
        lis[w]=lis[v]+1
        d.append(w)
  return lis

lis1 = bfs(target)
lis2 = bfs(v)
ans = 0
for i in range(N):
  if lis1[i]<lis2[i]:
    ans = max(ans, lis2[i]-1)
print(ans)