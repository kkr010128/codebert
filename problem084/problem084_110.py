#n = int(input())
from collections import deque
n, m = map(int, input().split())
# n=200000
# m=200000
#al = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
adjl = [[] for _ in range(n+1)]
NIL = -1
appear = {}
isalone = {}
for i in range(m):
    a, b = map(int, input().split())
    if appear.get((a, b), False) or appear.get((a, b), False):
        continue
    appear[(a, b)] = True
    appear[(b, a)] = True
    isalone[a] = False
    isalone[b] = False
    adjl[a].append(b)
    adjl[b].append(a)

NIL = -1  # 未発見を示す値
d = [-1 for i in range(n+1)]  # 頂点1からの距離を格納するリスト
color = [NIL for i in range(n+1)]  # 未到達かを示すリスト


def bfs(start_node, color_id):  # uは探索の開始点
    global color, d
    q = deque([start_node])
    d[start_node] = 0
    color[start_node] = color_id
    while len(q) != 0:
        u = q.popleft()
        for v in adjl[u]:
            if color[v] == NIL:
                d[v] = d[u]+1
                color[v] = color_id
                q.append(v)


color_id = 0
for u in range(1, n+1):
    if color[u] == NIL:
        color_id += 1
        bfs(u, color_id)

group = {}
for i in range(1, n+1):
    if isalone.get(i, True):
        continue
    group[color[i]] = group.get(color[i], 0)+1

mx = 1
for k, v in group.items():
    mx = max(mx, v)

print(mx)
