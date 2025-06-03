
import copy
import sys

# 再帰上限を引き上げる
sys.setrecursionlimit(10**6)

def dfs(graph, v, d):
    seen[v] = True # 訪問済みかどうか
    dist[v] = d # 距離を記録

    # 頂点vから行ける頂点を全探索
    for i in graph[v]:
        if seen[i]:
            continue
        dfs(graph, i, d+1)

# ここから本文
N, u, v = map(int, input().split())

u -= 1
v -= 1

# グラフ構造を作る
graph = [[] for i in range(N)]
for i in range(N - 1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    graph[A].append(B)
    graph[B].append(A)

# 青木くんからの各頂点の距離
seen = [False for i in range(N)]
dist = [0 for i in range(N)]
dfs(graph, v, 0)
aoki_dist = copy.deepcopy(dist)

# 高橋くんからの各頂点の距離
seen = [False for i in range(N)]
dist = [0 for i in range(N)]
dfs(graph, u, 0)
takahashi_dist = copy.deepcopy(dist)

ans = 0
for i in range(N):
    if aoki_dist[i] > takahashi_dist[i]:
        if aoki_dist[i] - 1 > ans:
            ans = aoki_dist[i] - 1      

print(ans)