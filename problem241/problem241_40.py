from collections import deque
m=[[1,0],[-1,0],[0,1],[0,-1]]
h,w=map(int,input().split())
l=list()
l.append('#'*(w+2))
for i in range(h):
    j=input()
    l.append('#'+j+'#')
l.append('#'*(w+2))
def bfs(a,b):
  s=[[-1 for j in i] for i in l]
  s[a][b]=0
  q=deque([[a,b]])
  while len(q)>0:
    x,y=q.popleft()
    for i,j in m:
      if l[x+i][y+j]=='.' and s[x+i][y+j]==-1:
        q.append([x+i,y+j])
        s[x+i][y+j]=s[x][y]+1
        num = s[x+i][y+j]
  return num
ans = []
for i in range(h+2):
  for j in range(w+2):
    if l[i][j] == '.':
      ans.append(bfs(i,j))
print(max(ans))