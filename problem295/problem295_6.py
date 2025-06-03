inf = 10**10
n,m,l = map(int,input().split())

def warshall_floyd(d):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                d[j][k] = min(d[j][k],d[j][i]+d[i][k])
    return d

G = [[inf] * n for _ in range(n)] #重み付きグラフ
for i in range(n):
    G[i][i] = 0
for _ in range(m):
    a,b,c = map(int,input().split())
    G[a-1][b-1] = c
    G[b-1][a-1] = c

G = warshall_floyd(G)
P = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            P[i][j] = 0
        elif G[i][j] <= l:
            P[i][j] = 1
        else:
            P[i][j] = inf

p = warshall_floyd(P)
q = int(input())

for _ in range(q):
    s,t = map(int,input().split())
    ans = p[s-1][t-1]-1
    print(ans if ans <= 10**9 else -1)