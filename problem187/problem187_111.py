# # -*- coding: utf-8 -*-

#
N, X, Y = map(int, input().split(' '))
edges = [(i, i+1) for i in range(N-1)]
graph = [{} for _ in range(N)]
for src, dst in edges:
    graph[src][dst] = 1
    graph[dst][src] = 1
graph[X-1][Y-1] = 1
graph[Y-1][X-1] = 1

import collections
d_frq_dict = collections.Counter()
for start in range(N):
    dist = [float('inf') for _ in range(N)]
    dist[start] = 0
    buf = [start]
    while buf:
        src = buf.pop(0)
        for dst in graph[src]:
            if dist[dst] == float('inf'):
                dist[dst] = dist[src] + 1
                buf.append(dst)

    d_frq_dict.update(dist)
    # print(dist)

for d in range(1, N):
    print(d_frq_dict[d]//2)
