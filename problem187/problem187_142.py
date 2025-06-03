from collections import deque

n, x, y = map(int, input().split())

graph = [[i-1,i+1] for i in range(n+1)]
graph[1]=[2]
graph[n]=[n-1]
graph[0]=[0]

graph[x].append(y)
graph[y].append(x)

def bfs(start,graph2):
    dist = [-1] * (n+1)
    dist[0] = 0
    dist[start] = 0

    d = deque()
    d.append(start)
    while d:
        v = d.popleft()
        for i in graph2[v]:
            if dist[i] != -1:
                continue
            dist[i] = dist[v] + 1
            d.append(i)
        
    dist = dist[start+1:]
    return dist

ans=[0 for _ in range(n-1)]
for i in range(1,n+1):
    for j in bfs(i,graph):
        ans[j-1] +=1
 
for i in ans:
    print(i)