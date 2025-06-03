import sys 
from collections import deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N,X,Y = map(int,readline().split())
ans = [0]*N
graph = [[] for _ in range(N)]
for i in range(N-1):
    graph[i].append(i+1)
    graph[i+1].append(i)
graph[X-1].append(Y-1)
graph[Y-1].append(X-1)

def bfs(x,q,dist):
    while q:
        v = q.popleft()
        for nx in graph[v]:
          if dist[nx] != 0:
            continue
          dist[nx] = dist[v] + 1
          q.append(nx)
          if nx > x:
            ans[dist[nx]] +=1

for i in range(N):
    dist = [0]*N
    q = deque([i])
    bfs(i,q,dist)
      
print('\n'.join(str(n) for n in ans[1:]))