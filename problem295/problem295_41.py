import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
INF = 10**18
G = [[INF]*N for i in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    if c <= L:
        G[a][b] = c
        G[b][a] = c
for k in range(N):
    for i in range(N):
        for j in range(N):
            G[i][j] = min(G[i][j], G[i][k]+G[k][j])
G2 = [[INF]*N for i in range(N)]
for i in range(N):
    for j in range(N):
        if G[i][j] <= L:
            G2[i][j] = 1
for k in range(N):
    for i in range(N):
        for j in range(N):
            G2[i][j] = min(G2[i][j], G2[i][k]+G2[k][j])
Q = int(input())
ans = []
for i in range(Q):
    s, t = map(int, input().split())
    s -= 1
    t -= 1
    if G2[s][t] == INF:
        ans.append(-1)
    else:
        ans.append(G2[s][t]-1)
print(*ans, sep="\n")
