from collections import deque


def matrix(n):
    for _ in range(n):
        adj = list(map(int, input().split()))
        i = adj[0]
        v = adj[2:]
        for j in v:
            mat[i - 1][j - 1] = 1


def bfs(v):
    d[v] = 1
    dist[v] = 0
    dq.append(v)
    while dq:
        v = dq.popleft()
        for n, i in enumerate(mat[v]):
            if i == 1 and not d[n]:
                d[n] = 1
                dist[n] = dist[v] + 1
                dq.append(n)

n = int(input())
mat = [[0] * n for _ in range(n)]
d, dist = [0] * n, [-1] * n
dq = deque()
matrix(n)
bfs(0)
for i, v in enumerate(dist):
    print(i + 1, v)