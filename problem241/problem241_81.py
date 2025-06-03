h,w=[int(x) for x in input().rstrip().split()]
l=[list(input()) for i in range(h)]
move=[[1,0],[-1,0],[0,-1],[0,1]]
def bfs(x,y):
  stack=[[x,y]]
  done=[[False]*w for i in range(h)]
  dist=[[0]*w for i in range(h)]
  max_val=0
  while(stack):
    nx,ny=stack.pop(0)
    done[ny][nx]=True
    for dx,dy in move:
      mx=nx+dx
      my=ny+dy
      if not(0<=mx<=w-1) or not(0<=my<=h-1) or done[my][mx]==True or l[my][mx]=="#":
        continue
      done[my][mx]=True
      dist[my][mx]=dist[ny][nx]+1
      max_val=max(max_val,dist[my][mx])
      stack.append([mx,my])
  return max_val

ans=0
for i in range(w):
  for j in range(h):
    if l[j][i]!="#":
      now=bfs(i,j)
      ans=max(ans,now)
print(ans) 