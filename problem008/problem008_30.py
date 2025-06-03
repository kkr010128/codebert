n = int(input())

from collections import deque

graph = [deque([]) for _ in range(n+1)]

for _ in range(n):
    u, k, *v = [int(x) for x in input().split()]

    v.sort()
    for i in v:
        graph[u].append(i)
    
arrive = [-1 for i in range(n+1)]
finish = [-1 for i in range(n+1)]

times = 0

def dfs(v):
    global times
    times += 1
    arrive[v] = times
    stack = [v]
    
    while stack:
        v = stack[-1]
        if graph[v]:
            w = graph[v].popleft()
            if arrive[w] == -1:
                times += 1
                arrive[w] = times
                stack.append(w)
        else:
            times += 1
            finish[v] = times
            stack.pop()
    return

for i in range(n):
    if arrive[i+1] == -1:
        dfs(i+1)

for j in range(n):
    tmp = [j+1, arrive[j+1], finish[j+1]]
    print(*tmp)

