from collections import deque

N = int(input())
graph = {i:[] for i in range(N)}

for i in range(N):
    g = list(map(int, input().split()))
    for j in range(g[1]):
        graph[g[0]-1].append(g[j+2]-1)
        
que = deque()
dist = [-1 for _ in range(N)]
que.append(0)
dist[0] = 0

while que:
    top = que.popleft()
    
    for i in graph[top]:
        if(dist[i] != -1):
            continue
        dist[i] = dist[top]+1
        que.append(i)

for i in range(len(dist)):
    print(i+1, dist[i])    
