import sys
input = sys.stdin.readline
inf = 1000
inf5 = 10**10
n, m, l = map(int, input().split())
graph = [[inf5] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

inf = 1000


def warshall_floyd(d):
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])


warshall_floyd(graph)

ans = [[inf] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] <= l:
            ans[i][j] = 1

warshall_floyd(ans)
q = int(input())
for _ in range(q):
    s, t = map(int, input().split())
    if ans[s][t] == inf:
        print(-1)
        continue
    print(ans[s][t] - 1)


