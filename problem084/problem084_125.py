import sys
import math
from collections import deque
n,m = map(int, input().split())

q = [0]*(n+1)

graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dist = [-1] * (n+1)
dist[0] = 0
dist[1] = 0

# if m == 0:
#     print(1)
#     exit()

d = deque()
a = 0
for l,j in enumerate(q):
    b = set()
    if j == 0:
        d.append(l)
        while d:
            v = d.popleft()
            b.add(v)
            q[v] = -1

            for i in graph[v]:
                b.add(i)
                q[i] = -1

                if dist[i] != -1:
                    continue
                dist[i] = dist[v] + 1
                d.append(i)
        a = max(a,len(b))
print(a)