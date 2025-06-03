import sys
sys.setrecursionlimit(10**7)

def dfs(f):
    if vis[f] == 1: return
    vis[f] = 1
    for t in V[f]:
        dfs(t)
          
          
n, m = map(int, input().split())
E = [[*map(lambda x: int(x)-1, input().split())] for _ in range(m)]
V = [[] for _ in range(n)]
for a, b in E: V[a].append(b); V[b].append(a)
ans = 0
vis = [0]*n

for a in range(n):
    if vis[a]==1:
      continue
    ans+=1
    dfs(a)
print(ans-1)
