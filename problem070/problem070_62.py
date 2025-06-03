import sys
sys.setrecursionlimit(10**5)

n,m=map(int,input().split())
g=[[] for i in range(10**5+10)]
for i in range(m):
  a,b=map(lambda x:int(x)-1, input().split())
  g[a].append(b)
  g[b].append(a)
chk=[-1]*n

def dfs(s,cnt):
  for u in g[s]:
    if chk[u]>-1: continue;
    chk[u]=cnt
    dfs(u,cnt)

cnt=0
for i in range(n):
  if chk[i]==-1:
    chk[i]=cnt
    dfs(i,cnt)
    cnt+=1
    
print(max(chk))