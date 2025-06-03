import sys
from collections import deque

n = int(sys.stdin.readline().strip())
edges = [[] for _ in range(n)]
for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().strip().split(" ")))
    for node in tmp[2:]:
        edges[tmp[0] - 1].append(node-1)
# print(edges)

distance = [0] * n
q = deque()
q.append((0, 0))
visited = set()
while q:
    node, d = q.popleft()
    # print(node, d)
    if node in visited:
        continue
    distance[node] = d
    visited.add(node)
    for next in edges[node]:
        # print("next", next)
        q.append((next, d + 1))

for i, d in enumerate(distance):
    if i == 0:
        print(1, 0)
    else:
        print(i + 1, d if d > 0 else -1)
