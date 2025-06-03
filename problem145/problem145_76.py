from collections import deque

N,M = map(int,input().split())
grap = [[] for _ in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    grap[a].append(b)
    grap[b].append(a)

dist = [-1] * (N +1)
dist[0] = 0
dist[1] = 0

d = deque()
d.append(1)

while d:
    v = d.popleft()
    for i in grap[v]:
        if dist[i] != -1:
            continue
        dist[i] = v
        d.append(i)

if -1 in dist:
    print('No')
else:
    print('Yes',*dist[2:],sep='\n')

