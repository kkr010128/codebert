from collections import deque

N = int(input())
nodes = []
G ={}
is_visited = {}
q = deque()

for _ in range(N):
    lst = list(map(int, input().split()))
    idx = lst[0]
    nodes.append(idx)
    is_visited[idx] = False
    degree = lst[1]
    if degree > 0:
        G[idx] = lst[2:]
    else:
        G[idx] = []

INF = 10**12
costs = [INF]*N
# bfs
# 初期queue
que = deque()  # 必要なものはnodeidと原点からの距離
que.append(1)
costs[0] = 0
while que:
    node_id = que.popleft()  # 先入れ先出し
    cost = costs[node_id-1]
    for next_id in G[node_id]:
        if (costs[next_id-1] == INF):
            que.append(next_id)
            costs[next_id-1] = cost + 1
        
for i in range(N):
    if costs[i] != INF:
        print(i+1, costs[i])
    else:
        print(i+1, -1)
