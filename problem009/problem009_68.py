import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(2 * 10**6)


def inpl():
    return list(map(int, input().split()))


N = int(input())

edge = {}
for _ in range(N):
    tmp = inpl()
    u, k = tmp[:2]
    edge[u] = tmp[2:]

d = {i: -1 for i in range(1, N + 1)}
d[1] = 0
Q = deque()
Q.append(1)
while Q:
    v = Q.popleft()
    for nv in edge[v]:
        if d[nv] != -1:
            continue
        d[nv] = d[v] + 1
        Q.append(nv)

for i in range(1, N + 1):
    print(i, d[i])

