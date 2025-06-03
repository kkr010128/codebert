import sys
input = sys.stdin.readline
N,M,L = map(int,input().split())
ABC = [tuple(map(int,input().split())) for i in range(M)]
Q = int(input())
ST = [tuple(map(int,input().split())) for i in range(Q)]

INF = float('inf')
ds = [[INF]*N for i in range(N)]
for a,b,c in ABC:
    a,b = a-1,b-1
    ds[a][b] = ds[b][a] = c
for i in range(N):
    ds[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            ds[i][j] = min(ds[i][j], ds[i][k]+ds[k][j])

ls = [[INF]*N for i in range(N)]
for i in range(N-1):
    for j in range(i+1,N):
        if ds[i][j] <= L:
            ls[i][j] = ls[j][i] = 1
for i in range(N):
    ls[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            ls[i][j] = min(ls[i][j], ls[i][k]+ls[k][j])

ans = []
for s,t in ST:
    ans.append(-1 if ls[s-1][t-1]==INF else ls[s-1][t-1] - 1)
print(*ans, sep='\n')