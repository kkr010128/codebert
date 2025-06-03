from collections import deque 

def bfs(G,dist,s):
    q = deque([])
    dist[s] = 0
    q.append(s)
    
    while len(q) > 0:
        v = q.popleft()
        
        for nv in G[v]:
            if dist[nv] != -1:
                continue
            
            dist[nv] = dist[v] + 1
            q.append(nv)
  


n,m = map(int,input().split())

G = [[] for _ in range(n)]

for i in range(m):
    a,b = map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

dist = [-1]*n

cnt = 0
for v in range(n):
    if dist[v] != -1:
        continue
    bfs(G,dist,v)
    cnt += 1
    
print(cnt-1)