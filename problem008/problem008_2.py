import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = {i: deque() for i in range(1, n+1)}
for _ in range(n):
    u, k, *v = [int(x) for x in input().split()]
    v.sort()
    for i in v:
        graph[u].append(i)
        #graph[i].append(u)

seen = [0]*(n+1)
stack = []
time = 0
seentime = [0]*(n+1)
donetime = [0]*(n+1)

def dfs(j):
    global time
    seen[j] = 1
    time += 1
    seentime[j] = time
    stack.append(j)
    while stack:
        s = stack[-1]
        if not graph[s]:
            stack.pop()
            time += 1
            donetime[s] = time
            continue
        g_NO  = graph[s].popleft()
        if seen[g_NO]:
            continue
        seen[g_NO] = 1
        stack.append(g_NO)
        time += 1
        seentime[g_NO] = time

for j in range(1, n+1):
    if seen[j]:
        continue
    dfs(j)

for k, a, b in zip(range(1, n+1), seentime[1:], donetime[1:]):
    print(k, a, b)
