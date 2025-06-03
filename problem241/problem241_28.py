from collections import deque

def BFS(s):
  q = deque()
  q.append(s)
  dist = [[10**10]*(W+2) for _ in range(H+2)]
  dist[s[0]][s[1]] = 0
  d = ((0,1),(0,-1),(1,0),(-1,0))
  far = []
  
  while len(q)>0:
    i,j = q.popleft()
    for di,dj in d:
      if field[i+di][j+dj] == "." and dist[i+di][j+dj] == 10**10:
        q.append([i+di,j+dj])
        dist[i+di][j+dj] = dist[i][j]+1
    res = dist[i][j]
  
  return res



H,W = map(int,input().split())
field = ["#"*(W+2)]
field += ["#"+input()+"#" for _ in range(H)]
field += ["#"*(W+2)]
res = 0

for i in range(H+2):
  for j in range(W+2):
    if field[i][j] == ".":
      s = [i,j]
      res = max(res,BFS(s))
      
print(res)