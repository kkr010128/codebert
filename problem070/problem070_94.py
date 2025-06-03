from collections import defaultdict

def bfs(s):
  q = [s]
  while q != []:
    p = q[0]
    del q[0]
    for node in adj[p]:
      if not visited[node]:
        visited[node] = True
        q.append(node)

n,m = map(int,input().split())
adj = defaultdict(list)
visited = [False]*(n+1)
comp = 0
for _ in range(m):
  a,b = map(int,input().split())
  adj[a].append(b)
  adj[b].append(a)
for i in range(1,n+1):
  if not visited[i]:
    comp+=1
    bfs(i)
print(comp-1)