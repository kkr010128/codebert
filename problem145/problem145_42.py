from collections import deque
n,m=map(int,input().split())
g=[[] for i in range(n)]
mark=[0]*n
for i in range(m):
  a,b=map(int,input().split())
  a-=1;b-=1
  g[a].append(b)
  g[b].append(a)
D=deque([0])
visited=[False]*n
visited[0]=True
while D:
  v=D.popleft()
  for i in g[v]:
    if visited[i]:
      continue
    visited[i]=True
    mark[i]=v
    D.append(i)
print("Yes")
for i in range(1,n):
  print(mark[i]+1)