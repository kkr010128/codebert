from collections import deque

def dfs(v):
    global t
    
    d[v] = t
    visited[v] = True
    t += 1
    
    for u in graph[v]:
        if not visited[u]: dfs(u)
    f[v] = t
    t += 1
    
    
n = int(input())
graph = [deque() for i in range(n)]

visited = [False] * n
d = [0] * n
f = [0] * n
t = 1

for i in range(n):
    nums = list(map(int, input().split()))
    for j in nums[2:]:
        graph[i].append(j-1)
         
for i in range(n):
    if not visited[i]: dfs(i)

for idx, df in enumerate(zip(d, f)):
    print(idx+1, df[0], df[1])

