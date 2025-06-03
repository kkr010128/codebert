import sys
from heapq import heapify, heappop, heappush

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, U, V = lr()
graph = [[] for _ in range(N+1)] # 1-indexed
for _ in range(N-1):
    a, b = lr()
    graph[a].append(b)
    graph[b].append(a)

def dijkstra(start):
    INF = 10 ** 15
    dist = [INF] * (N+1)
    dist[start] = 0
    que = [(0, start)]
    while que:
        d, prev = heappop(que)
        if dist[prev] < d:
            continue
        for next in graph[prev]:
            d1 = d + 1
            if dist[next] > d1:
                dist[next] = d1
                heappush(que, (d1, next))
    return dist

dist_U = dijkstra(U)
dist_V = dijkstra(V)
answer = max(v for u, v in zip(dist_U, dist_V) if v > u) - 1
print(answer)
# 25