from collections import deque
import copy

h,w=map(int,input().split())
Inf=float('inf')
maze1=[]
for _ in range(h):
  s=list(input())
  for u in range(w):
    if s[u]=='.':
      s[u]=Inf
  maze1.append(s)
  
def maze_solve(maze,sy,sx):
  qu=deque([[sy,sx]])
  maze[sy][sx]=0
  
  while qu:
    y,x=qu.popleft()
    
    T=maze[y][x]
    for i in ([1,0],[-1,0],[0,1],[0,-1]):
      ny=y+i[0]
      nx=x+i[1]
      if 0<=ny<=h-1 and 0<=nx<=w-1 and maze[ny][nx]!='#':
        
        if maze[ny][nx]>T+1:
          maze[ny][nx]=T+1
          qu.append([ny,nx])
          
  ans=-Inf
  for i in range(h):
    for j in range(w):
      if maze[i][j]!='#' and maze[i][j]!=Inf:
        ans=max(ans,maze[i][j])
  return ans
  

ans=-Inf
for i in range(h):
  for j in range(w):
    if maze1[i][j]!='#':
      maze2=copy.deepcopy(maze1)
      ans=max(ans,maze_solve(maze2,i,j))
            
            
print(ans)