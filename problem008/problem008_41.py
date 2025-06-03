def dfs(v):
    global t, d, f, visited
    d[v] = t
    visited[v] = True
    t += 1
    for u in AL[v]:
        if not visited[u]:
            dfs(u)
    f[v] = t
    t += 1

# 入力
n = int(input())
AL = [[] for _ in range(n + 1)]
for v in range(1, n + 1):
    AL[v] = [int(x) for x in input().split()][2:]

# 計算
d = [0] * (n + 1)
f = [0] * (n + 1)
t = 1
visited = [False] * (n + 1)
for v in range(1, n + 1):
    if not visited[v]:
        dfs(v)

# 出力
for v in range(1, n + 1):
    print(v, d[v], f[v])

