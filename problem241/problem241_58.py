from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))
from copy import deepcopy
from collections import deque

h,w=nii()
s=[list(input()) for i in range(h)]

def dfs(cs,i,j):
  que=deque()
  que.append([i,j])

  cs[i][j]='#'

  dist=[[-1 for a in range(w)] for b in range(h)]
  dist[i][j]=0

  while que:
    y,x=que.popleft()
    for dy,dx in [[1,0],[-1,0],[0,1],[0,-1]]:
      ny=y+dy
      nx=x+dx
      if 0<=ny<h and 0<=nx<w and cs[ny][nx]=='.':
        que.append([ny,nx])
        cs[ny][nx]='#'
        dist[ny][nx]=dist[y][x]+1

  t_ans=0
  for a in dist:
    t_ans=max(t_ans,max(a))

  return t_ans

ans=0
for i in range(h):
  for j in range(w):
    if s[i][j]=='.':
      cs=deepcopy(s)
      dist=dfs(cs,i,j)
      ans=max(ans,dist)

print(ans)