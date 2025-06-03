# https://qiita.com/takayg1/items/7008e4c9584e42ae13c7

from collections import deque

N, M = (int(i) for i in input().split())

graph = [deque([]) for _ in range(N + 1)]
for _ in range(M):
    a, b = (int(i) for i in input().split())
    graph[a].append(b)
    graph[b].append(a)


seen = [-1] * (N + 1) 

def dfs(v):
    stack = [v]
    while stack:
        v = stack[-1]
        if graph[v]:
            w = graph[v].popleft()
            if seen[w] < 0:
                seen[w] = 0
                stack.append(w) 
        else:
            stack.pop()

ans = 0
for i in range(N):
    if seen[i + 1] < 0:
        dfs(i + 1)
        ans += 1

print(ans - 1)