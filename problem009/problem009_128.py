from collections import deque
def bfs(g,v):
    q=deque([v]) ; vis=[0]*n
    vis[v]=1 ; stg[v]=0
    while q:
        v=q[0]
        for p in g[v]:
            if vis[p]==0: 
                q.append(p)
                vis[p]=1
                stg[p]=stg[v]+1
        q.popleft()
n=int(input())
g=[[] for i in range(n)]
for _ in range(n):
    a=[int(i)-1 for i in input().split()]
    for i in a[2:]: g[a[0]].append(i)
stg=[-1]*n
bfs(g,0)
for i in range(n):
    print(i+1,stg[i])
    

