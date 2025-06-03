from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = [0]*(n-1)

d = deque()
d.append(1)

while d:
    v = d.popleft()
    for i in graph[v]:
        if ans[i-2] != 0 or i == 1:
            continue
        ans[i-2] = v
        d.append(i)
        
print('Yes')
print(*ans, sep='\n')