from collections import deque
n = int(input())
G = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    u = tmp.pop(0)
    k = tmp.pop(0)
    t = []
    for i in range(k):
        a = tmp.pop(0)
        t.append(a-1)
    G.append(t)
    
dist = [-1]*n
dist[0] = 0
que = deque()
que.append(0)

while que:
    v = que.popleft()
    for nv in G[v]:
        if dist[nv] != -1:
            continue
        dist[nv] = dist[v] + 1
        que.append(nv)
    
for i in range(n):
    print(i+1, dist[i])
