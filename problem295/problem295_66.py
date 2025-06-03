N, M, L = map(int, input().split())
dist = [[10**12] * N for _ in range(N)]
for i in range(N):
    dist[i][i] = 0
    
for _ in range(M):
    a, b, c = map(int, input().split())
    if c <= L:
    	dist[a-1][b-1] = dist[b-1][a-1] = c

for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

old_dist = [row[:] for row in dist]
for i in range(N):
    for j in range(N):
        if old_dist[i][j] <= L:
            dist[i][j] = 1
            
for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

Q = int(input())
for _ in range(Q):
    start, end= map(int, input().split())
    if dist[start-1][end-1] < 10**12:
    	print(dist[start-1][end-1] - 1)
    else:
        print(-1)