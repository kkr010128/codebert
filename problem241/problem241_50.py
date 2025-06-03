H,W = list(map(int,input().split()))
N=H*W

#壁のノード
wall=[]
for h in range(H):
    for w_idx,w in enumerate(list(input())):
        if w == '#':
            wall.append(W*h+w_idx+1)
#道のノード        
path=[_ for _ in range(1,N+1) if _ not in wall]

#隣接リスト
ad = {}
for n in range(N):
    ad[n+1]=[]
    
for n in range(N):
    n=n+1
    if n not in wall:
        up = n-W
        if up > 0 and up not in wall:
            ad[n].append(up)
            
        down = n+W
        if down <= N and down not in wall:
            ad[n].append(down)
            
        left = n-1
        if n % W != 1 and left not in wall and left > 0:
            ad[n].append(left)
        
        right = n+1
        if n % W != 0 and right not in wall:
            ad[n].append(right)      

from collections import deque

def BFS(start):
    que = deque([start])
    visit = deque([])

    color = {}
    for n in range(N):
        color[n+1] = -1
    color[start] = 0

    depth = {}
    for n in range(N):
        depth[n+1] = -1

    depth[start] = 0
    while len(que) > 0:
        start = que[0]
        for v in ad[start]:
            if color[v] == -1:
                que.append(v)
                color[v] = 0
                depth[v] = depth[start]+1

        color[start] = 1
        visit.append(que.popleft())

    return depth[start]

ans=-1
for start in path:
    ans_=BFS(start)
    if ans < BFS(start):
        ans = ans_
    
#     print(start,ans_)
    
print(ans)