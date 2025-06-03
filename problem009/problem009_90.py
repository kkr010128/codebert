import sys

n = int(input())
G = [None]*n
for i in range(n):
    u, k, *vs = map(int, input().split())
    G[u-1] = [e-1 for e in vs]

from collections import deque
dist = [-1]*n
que = deque([0])
dist[0] = 0
while que:
    v = que.popleft()
    d = dist[v]
    for w in G[v]:
        if dist[w] > -1: #already visited
            continue
        dist[w] = d + 1
        que.append(w)

for i in range(n):
    print(i+1, dist[i])
