from collections import deque
import sys
input = sys.stdin.readline


N = int(input())
G = [[] for _ in range(N)]
for _ in range(N):
    ls = list(map(int, input().split()))
    u = ls[0] - 1
    for v in ls[2:]:
        G[u].append(v - 1)

time = 1
d = [None for _ in range(N)]
f = [None for _ in range(N)]

def dfs(v):
    global time
    d[v] = time
    time += 1
    
    for u in range(N):
        if u in G[v]:
            if d[u] is None:
                dfs(u)

    f[v] = time
    time += 1

for v in range(N):
    if d[v] is None:
        dfs(v)

for v in range(N):
    print("{} {} {}".format(v + 1, d[v], f[v]))
