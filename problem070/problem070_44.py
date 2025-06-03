import sys
sys.setrecursionlimit(10**7+1)

N,M = map(int,input().split())
V = [i for i in range(N)]
E =[[] for i in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    E[a-1].append(b-1)
    E[b-1].append(a-1)
visited = [False for _ in range(N)]
def dfs(v,parent,origin):
    visited[v] = True
    for e in E[v]:
        if e == parent:
            continue
        if visited[e]:
            continue
        V[e] = origin
        dfs(e,v,origin)

for i in range(N):
    if visited[i]:
        continue
    dfs(i,-1,i)
count = 0
for i,v in enumerate(V):
    if i==v:
        count+=1

print(count-1)



