h,w=map(int,input().split())
g=[[*input()] for _ in range(h)]
from collections import *
a=0
for sx in range(h):
  for sy in range(w):
    if g[sx][sy]=='#': continue
    d=[[-1]*w for _ in range(h)]
    d[sx][sy]=0
    q=deque([(sx,sy)])
    while q:
      x,y=q.popleft()
      t=d[x][y]+1
      for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
        nx,ny=x+dx,y+dy
        if 0<=nx<h and 0<=ny<w and g[nx][ny]=='.' and d[nx][ny]<0:
          d[nx][ny]=t
          q.append((nx,ny))
          a=max(a,t)
print(a)