from collections import deque
import numpy as np
H,W = map(int,input().split())
maze = [input() for _ in range(H)]
ans = 0
for x in range(H):
  for y in range(W):
    if maze[x][y]=='#':
      continue
    dist = [[0]*W for i in range(H)]
    Q = deque([[x,y]])
    while Q:
      h,w = Q.popleft()
      for i,j in [[1,0],[-1,0],[0,1],[0,-1]]:
        h2,w2 = h+i,w+j
        if 0<=h2<H and 0<=w2<W and dist[h2][w2]==0 and maze[h2][w2]!='#':
          dist[h2][w2] = dist[h][w]+1
          Q.append([h2,w2])
    dist[x][y] = 0
    ans = max(ans, np.max(dist))
print(ans)