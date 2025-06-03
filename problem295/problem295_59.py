import sys
input = sys.stdin.readline
N, m, l = map(int, input().split())
graph = [[] for i in range(N+1)]

INF = 2 ** 31 - 1
d = [[INF for i in range(N+1)] for j in range(N+1)]
for i in range(N+1):
    d[i][i] = 0
for i in range(m):
    a, b, c = map(int, input().split())
    d[a][b] = c
    d[b][a] = c


for k in range(N+1):
    for i in range(N+1):
        for j in range(N+1):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

d2 = [[INF for i in range(N+1)] for j in range(N+1)]
for i in range(N+1):
    d[i][i] = 0

for i in range(N+1):
    for j in range(N+1):
        if d[i][j] <= l:
            d2[i][j] = 1

for k in range(N+1):
    for i in range(N+1):
        for j in range(N+1):
            d2[i][j] = min(d2[i][j], d2[i][k] + d2[k][j])


q = int(input())
for i in range(q):
    s, t = map(int, input().split())
    if d2[s][t] == INF:
        print(-1)
    else:
        print(d2[s][t] - 1)
