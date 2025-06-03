import heapq
INFTY = 10**4
N,X,Y = map(int,input().split())
G = {i:[] for i in range(1,N+1)}
for i in range(1,N):
    G[i].append(i+1)
    G[i+1].append(i)
G[X].append(Y)
G[Y].append(X)
dist = [[INFTY for _ in range(N+1)] for _ in range(N+1)]
for i in range(N+1):
    dist[i][i] = 0
for i in range(1,N+1):
    hist = [0 for _ in range(N+1)]
    heap = [(0,i)]
    hist[i] = 1
    while heap:
        d,x = heapq.heappop(heap)
        if d>dist[i][x]:continue
        hist[x] = 1
        for y in G[x]:
            if hist[y]==0:
                if dist[i][y]>d+1:
                    dist[i][y] = d+1
                    heapq.heappush(heap,(d+1,y))
C = {k:0 for k in range(1,N)}
for i in range(1,N):
    for j in range(i+1,N+1):
        C[dist[i][j]] += 1
for k in range(1,N):
    print(C[k])