import sys
input = sys.stdin.readline

n, m, l = map(int, input().split())
INF = float("inf")

def warshall_floyd(d, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

d = [[INF] * n for _ in range(n)]
for i in range(n):
    d[i][i] = 0
for i in range(m):
    a, b, c = map(int, input().split())
    d[a - 1][b - 1] = c
    d[b - 1][a - 1] = c
d = warshall_floyd(d, n)

d2 = [[INF] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if d[i][j] <= l:
            d2[i][j] = 1
    d2[i][i] = 0
d2 = warshall_floyd(d2, n)

q = int(input())
for _ in range(q):
    s, t = map(int, input().split())
    res = d2[s - 1][t - 1]
    print(-1 if res == INF else res - 1)