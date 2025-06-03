from collections import deque

INF = 1e9

def BFS(n, adj):
    d = [INF] * N
    d[0] = 0
    next_v = deque([0]) # ?¬??????????????????????
    
    while next_v:
        u = next_v.popleft()
        
        for v in adj[u]:
            if d[v] == INF:
                d[v] = d[u] + 1
                next_v.append(v)
    
    return d

N = int(input())
Adj = [None] * N

for i in range(N):
    u, k, *vertex = [int(i)-1 for i in input().split()]
    Adj[u] = vertex

distance = BFS(N, Adj)

for i, di in enumerate(distance, start = 1):
    if di == INF:
        print(i, -1)
    else:
        print(i, di)