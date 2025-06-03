#!/usr/bin/env python

import queue

def dfs(node, edge, vis):
    vis[node] = True
    count = 1
    vq = []
    vq.append(node)
    vq = queue.LifoQueue()
    vq.put(node)
    while not vq.empty():
        fnode = vq.get()
        for b in edge[fnode]:
            if not vis[b]:
                count += 1
                vq.put(b)
                vis[b] = True
    return count

n, m = [int(i) for i in input().split(' ')]

edge = [[] for i in range(n)]

for _ in range(m):
    a, b = [int(i) for i in input().split(' ')]
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)

vis = [False]*n

count = 0

for i in range(n):
    if not vis[i]:
        count = max(count, dfs(i, edge, vis))

print(count)
