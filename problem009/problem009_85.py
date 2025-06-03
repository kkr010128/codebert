from collections import deque
u = int(input())
g = [[i for i in map(int, input().split())] for _ in range(u)]
graph = [[] for _ in range(u)]
ans = [-1] * u
for i in range(u):
    for j in range(g[i][1]):
        graph[i].append(g[i][2 + j] - 1)
que = deque()
que.append(0)
ans[0] = 0
while que:
    v = que.popleft()
    for nv in graph[v]:
        if ans[nv] != -1:
            continue
        ans[nv] = ans[v] + 1
        que.append(nv)

for i in range(u):
    print(i+1, ans[i])

