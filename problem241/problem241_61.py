from collections import deque
def bfs(sy,sx):
  q=deque([[sy,sx]])
  visited[sy][sx]=0
  while q:
    y,x=q.popleft()
    for dy,dx in ([1,0],[-1,0],[0,1],[0,-1]):
      ny,nx=y+dy,x+dx
      if ny<0 or ny>h-1 or nx<0 or nx>w-1 or path[ny][nx]=="#":continue
      if path[ny][nx]=="." and visited[ny][nx]==-1:
        visited[ny][nx]=visited[y][x]+1
        q.append([ny,nx])
  res=-1
  for i in range(h):
    for j in range(w):
      res=max(visited[i][j],res)
  return res

h,w=map(int,input().split())
path=[input() for i in range(h)]
visited=[[-1]*w for i in range(h)]
sy,sx=0,0
gy,gx=0,0
ans=0
for i in range(h):
  for j in range(w):
    if path[i][j]=="#":continue
    sy=i
    sx=j
    visited=[[-1]*w for _ in range(h)]
    t=bfs(sy,sx)
    ans=max(t,ans)
print(ans)

