from collections import deque
import _pickle as cPickle
import cProfile
H, W =map(int,input().split())
grid = [input() for i in range(H)]
dist = [[-1]*W for _ in range(H)]

cells = deque()
for h in range(H):
    for w in range(W):
        if grid[h][w] == '.':
            dist[h][w] = 0
            cells.append((h,w))

distG = cPickle.loads(cPickle.dumps(dist, -1))
pcells = deque()
def bfs(h,w):
    pcells.append((h,w))
    d = 1
    distG[h][w] = 1
    while pcells:
        oh,ow = pcells.popleft()
        d = distG[oh][ow]
        for dx, dy in ((0,1),(0,-1),(1,0),(-1,0)):
            nw = ow + dx
            nh = oh + dy
            if nw < 0 or W <= nw or nh <0 or H <= nh:
                continue
            if distG[nh][nw] == 0:
                distG[nh][nw] = d+1
                pcells.append((nh,nw))

    return d-1

a = 0
for i in range(len(cells)):
    distG = cPickle.loads(cPickle.dumps(dist, -1))
    h,w = cells.popleft()
    a = max(a,bfs(h,w))
print(a)