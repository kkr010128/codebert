import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


n, u, v = map(int, input().split())

GRAPH = {i:[] for i in range(1, n + 1)}
for _ in range(n - 1):
    a, b = map(int, input().split())
    GRAPH[a].append(b)
    GRAPH[b].append(a)

def dfs(now, prev = 0):
    PARENT[now] = prev
    DEPTH[now] = DEPTH[prev] + 1
    if len(GRAPH[now]) == 1:
        LEAVES.append((DEPTH[now], now))
    
    for w in GRAPH[now]:
        if w == prev:
            continue
        next = w
        dfs(next, now)

PARENT = {}
DEPTH = {0:-1}
LEAVES = []
dfs(v)

PATH = {i:False for i in range(1, n + 1)}
now = u
while True:
    PATH[now] = True
    if now == v:
        break
    now = PARENT[now]

LEAVES.sort(reverse = True)
for leaf in LEAVES:
    now = leaf[1]
    while True:
        if PATH[now]:
            break
        now = PARENT[now]
    lca = now
    
    du, dv = DEPTH[u] - DEPTH[lca], DEPTH[lca]
    if du < dv:
        print(leaf[0] - 1)
        exit()
