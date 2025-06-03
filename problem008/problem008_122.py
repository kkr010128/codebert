from collections import deque

N = int(input())
graph = [deque([]) for _ in range((N + 1))]
for _ in range(N):
    u, k, *v = [int(x) for x in input().split()]
    v.sort()
    for i in v:
        graph[u].append(i)
        
time = 0
arrive_time = [-1] * (N + 1)
finish_time = [-1] * (N + 1)

def dfs(v):
    global time
    time += 1
    stack = [v]
    arrive_time[v] = time
    while stack:
        v = stack[-1]
        if graph[v]:
            w = graph[v].popleft()
            if arrive_time[w] < 0:
                time += 1
                arrive_time[w] = time
                stack.append(w)
        else:
            time += 1
            finish_time[v] = time
            stack.pop()
    return [arrive_time, finish_time]
    
for i in range(N):
    if arrive_time[i + 1] < 0:
        ans = dfs(i + 1)
        
for j in range(N):
    temp = [j + 1, ans[0][j + 1], ans[1][j + 1]]
    print(*temp)
