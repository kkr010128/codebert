from collections import deque

n = int(input())
graph = [list(map(int,input().split()))[2:] for _ in range(n)]

dist = [-1]*(n+1)
dist[0] = 0
dist[1] = 0
d = deque()
d.append(1)

while d:
    v = d.popleft()-1
    if len(graph[v]) >= 1:
        for i in graph[v]:
            if dist[i] == -1:
                dist[i] = dist[v+1]+1
                d.append(i)

for i in range(1,n+1):
    print(i,dist[i])
