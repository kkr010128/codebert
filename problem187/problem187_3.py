from collections import deque

n,x,y = map(int,input().split())

adj = [[] for i in range(n)]

adj[x-1].append(y-1)
adj[y-1].append(x-1)

for i in range(n-1):
    adj[i].append(i+1)
    adj[i+1].append(i)

ans = [0]*(n-1)
for i in range(n):
    q = deque([])
    q.append(i)

    dist = [-1]*n
    dist[i] = 0

    while len(q) > 0:
        v = q.popleft()
    
        for nv in adj[v]:
            if dist[nv] != -1:
                continue
        
            dist[nv] = dist[v] + 1
            q.append(nv)
    for i in dist:
        if i != 0:
            ans[i-1] += 1

for i in ans:
    print(i//2)