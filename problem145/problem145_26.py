from collections import deque
n,m = map(int,input().split())
g = [[] for _ in range(n)]
for i in range(m):
    a,b = map(lambda x:int(x)-1,input().split())
    
    g[a].append(b)
    g[b].append(a) 
to = {}   
dist = [-1 for _ in range(n)]
dist[0] = 0
q = deque()
q.append(0)
while (len(q) > 0):
    v = q.popleft()
    for nv in g[v]:
        if (dist[nv] != -1):continue
        dist[nv] = dist[v] + 1
        q.append(nv)
        to[nv] = v
        
print('Yes')
for i in range(1,n):
    print(to[i]+1)