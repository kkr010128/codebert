from collections import deque
def bfs(y,x):
  q=deque([(y,x)])
  visited[y][x]=0
  while q:
    cy,cx=q.popleft()
    for dy,dx in [(1,0),(-1,0),(0,1),(0,-1)]:
      ny,nx=cy+dy,cx+dx
      if 0<=ny<h and 0<=nx<w and visited[ny][nx]==-1:
        if s[ny][nx]=="#":continue
        visited[ny][nx]=visited[cy][cx]+1
        q.append((ny,nx))
  res=0
  for i in range(h):
    for j in range(w):
      if s[i][j]!="#":
        res=max(res,visited[i][j])
  return res

h,w=map(int,input().split())
s=[input() for _ in range(h)]
ans=0
for i in range(h):
  for j in range(w):
    if s[i][j]=="#":continue
    sh=i
    sw=j
    visited=[[-1]*w for _ in range(h)]
    ans=max(ans,bfs(sh,sw))
print(ans)

