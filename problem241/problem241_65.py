import numpy as np
import queue
H,W=map(int,input().split())
S=list()
for i in range(H):
  S.append(input())
ans=0
  
for i in range(H):
  for j in range(W):
    if S[i][j]==".":
      L=[[-1]*W for i in range(H)]
      L[i][j]=0
      q=queue.Queue()
      q.put([i,j])
      while not q.empty():
        r=q.get()
        for k,l in [[1,0],[0,-1],[0,1],[-1,0]]:
          if r[0]+k>=0 and r[0]+k<H and r[1]+l>=0 and r[1]+l<W and S[r[0]+k][r[1]+l]=="." and L[r[0]+k][r[1]+l]==-1:
            L[r[0]+k][r[1]+l]=L[r[0]][r[1]]+1
            q.put([r[0]+k,r[1]+l])
      ans=max(ans,max(list(map(lambda x:max(x),L))))
print(ans)
