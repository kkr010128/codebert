import sys
input = sys.stdin.readline
N,M,L = map(int,input().split())
ABC = [tuple(map(int,input().split())) for i in range(M)]
Q = int(input())
ST = [tuple(map(int,input().split())) for i in range(Q)]

INF = 10**20
g = [[INF]*N for _ in range(N)]
for a,b,c in ABC:
    a,b = a-1,b-1
    g[a][b] = g[b][a] = c
for i in range(N):
    g[i][i] = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            if g[i][j] > g[i][k] + g[k][j]:
                g[i][j] = g[i][k] + g[k][j]

h = [[N]*N for _ in range(N)]
for i in range(N-1):
    for j in range(i+1,N):
        if g[i][j] <= L:
            h[i][j] = h[j][i] = 1
for i in range(N):
    h[i][i] = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            if h[i][j] > h[i][k] + h[k][j]:
                h[i][j] = h[i][k] + h[k][j]

ans = []
for s,t in ST:
    s,t = s-1,t-1
    if h[s][t] == N:
        ans.append(-1)
    else:
        ans.append(h[s][t] - 1)
print(*ans, sep='\n')