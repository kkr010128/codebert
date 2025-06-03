import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, M, L = lr()
INF = 10 ** 19
dis = [[INF for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    a, b, c = lr()
    if c > L:
        continue
    dis[a][b] = c
    dis[b][a] = c

for k in range(N+1): # kが中継地点
    for i in range(N+1):
        for j in range(i+1, N+1):
            x = dis[i][k] + dis[k][j]
            if x < dis[i][j]:
                dis[i][j] = dis[j][i] = x

supply = [[INF] * (N+1) for _ in range(N+1)]
for i in range(N+1):
    for j in range(i+1, N+1):
        if dis[i][j] <= L:
            supply[i][j] = supply[j][i] = 1

for k in range(N+1): # kが中継地点
    for i in range(N+1):
        for j in range(i+1, N+1):
            y = supply[i][k] + supply[k][j]
            if y < supply[i][j]:
                supply[i][j] = supply[j][i] = y

Q = ir()
for _ in range(Q):
    s, t = lr()
    if supply[s][t] == INF:
        print(-1)
    else:
        print(supply[s][t] - 1)

# 59 