from collections import deque
import numpy as np
H,W = map(int,input().split())
Maze=[list(input()) for i in range(H)]
ans=0
for hi in range(0,H):
    for wi in range(0,W):
        if Maze[hi][wi]=="#":
            continue
        maze1=[[0]*W for _ in range(H)]
        stack=deque([[hi,wi]])
        while stack:
            h,w=stack.popleft()
            for i,j in [[1,0],[-1,0],[0,1],[0,-1]]:
                new_h,new_w=h+i,w+j
                if new_h <0 or new_w <0 or new_h >=H or new_w >=W:
                    continue
                elif Maze[new_h][new_w]!="#" and maze1[new_h][new_w]==0:
                    maze1[new_h][new_w]=maze1[h][w]+1
                    stack.append([new_h,new_w])
        
        maze1[hi][wi]=0
        ans=max(ans,np.max(maze1))
print(ans)