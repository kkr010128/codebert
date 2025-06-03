from collections import deque
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)
    
dist = [-1] * (N+1)
dist[0] = 0

disjoint_set = []
n_disj = 0
d = deque()

for j in range(1,N+1):
    if dist[j] != -1:
        continue
    
    dist[j] = 0
    d.append(j)
    disjoint_set.append([])
    disjoint_set[n_disj].append(j)
        
    while d:
        v = d.popleft()
        for i in graph[v]:
            if dist[i] != -1:
                continue
            dist[i] = dist[v] + 1
            d.append(i)
            disjoint_set[n_disj].append(i)

    n_disj+=1
    
ans = 1
for s in disjoint_set:
    ans = max(ans, len(s))
print(ans)