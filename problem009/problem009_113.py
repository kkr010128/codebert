from sys import stdin
from collections import deque
n = int(stdin.readline())
d = [-1] * (n + 1)
def bfs(G):
    d[1] = 0
    queue = [1]
    dq = deque([1])
    while len(dq) > 0:
        v = dq.popleft()
        for c in G[v]:
            if d[c] < 0:
                d[c] = d[v] + 1
                dq.append(c)
    for i, x in enumerate(d[1:], start=1):
        print(i, x)
G = {}
for i in range(n):
    x = list(map(int, stdin.readline().split()))
    G[x[0]] = x[2:]
bfs(G)