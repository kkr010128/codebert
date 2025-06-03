N,M,L = map(int,input().split())
INF = 10**18
d = [[INF for j in range(N)] for i in range(N)]

# 入力
for _ in range(M):
    A,B,C = map(int,input().split())
    if L < C:
        continue
    d[A-1][B-1] = C
    d[B-1][A-1] = C

# 初期化
for i in range(N):
    d[i][i] = 0

# ワーシャルフロイド1回目
for k in range(N):
    for i in range(N):
        for j in range(N):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

for i in range(N):
    for j in range(N):
        if d[i][j] <= L:
            d[i][j] = 1
        else:
            d[i][j] = INF

# 初期化
for i in range(N):
    d[i][i] = 0

# ワーシャルフロイド2回目
for k in range(N):
    for i in range(N):
        for j in range(N):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

Q = int(input())

for _ in range(Q):
    s,t = map(int,input().split())
    if d[s-1][t-1] == INF:
        print(-1)
    else:
        print(d[s-1][t-1]-1)

