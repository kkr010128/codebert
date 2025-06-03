# 深さ優先探索 Depth first search: DFS


def dfs(u):
    global time
    color[u - 1] = 0
    time += 1
    d[u - 1] = time
    for v in range(1, n + 1):
        if A[u - 1][v - 1] == 1 and color[v - 1] == -1:
            dfs(v)
    color[u - 1] = 1
    time += 1
    f[u - 1] = time


n = int(input())
A = [[0 for i in range(n)] for i in range(n)]
for i in range(n):
    dat = [int(j) for j in input().split()]
    for j in range(dat[1]):
        A[dat[0] - 1][dat[2 + j] - 1] = 1

color = [-1 for i in range(n)]
d = [-1 for i in range(n)]
f = [-1 for i in range(n)]
time = 0
for i in range(n):
    if color[i] == -1:
        dfs(i+1)

for id in range(n):
    print(id + 1, d[id], f[id])

