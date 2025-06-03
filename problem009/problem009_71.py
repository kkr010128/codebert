n = int(input())
E = [[]]*n

for i in range(n):
    inputs = list(map(int, input().split()))
    if inputs[1]>0:
        for e in inputs[2:]:
            E[i] = E[i] + [e-1]

visited = [-1]*n
dist = [-1]*n
dist[0] = 0

from collections import deque

d = deque()
d.append(0)
visited[0] = 1

while len(d):
    nd = d.popleft()
    #print(nd, E[nd])
    for e in E[nd]:
        #print(e)
        if visited[e]<0:
            d.append(e)
            dist[e] = dist[nd] + 1
            visited[e] = 1
    #print(d, visited, dist, len(d))
            

for i in range(n):
    print(i+1, dist[i])
