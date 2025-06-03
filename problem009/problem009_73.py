from collections import deque
n = int(input())

g = [[] for _ in range(n)]
for i in range(n):
    _, _, *edge = map(lambda x: int(x)-1, input().split())

    g[i] = edge

q = deque()
q.append(0)
dist = [-1 for _ in range(n)]
dist[0] = 0

while(len(q) > 0):
    v = q.popleft()

    for nv in g[v]:
        if(dist[nv] != -1): continue
        
        dist[nv] = dist[v] + 1
        q.append(nv)

for i in range(n):
    print(i+1, dist[i])
