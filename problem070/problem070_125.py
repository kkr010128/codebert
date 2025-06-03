import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

from collections import defaultdict

n,m=map(int,input().split())
visited=[0]*n
d=defaultdict(list)
def dfs(n):
    visited[n]=1
    #print(visited)
    for i in d[n]:
        if visited[i]==0:
            dfs(i)

for i in range(m):
    a,b=map(int,input().split())
    a,b=a-1,b-1
    d[a].append(b)
    d[b].append(a)

r=-1
for i in range (n):
    if visited[i]==0:
        dfs(i)
        r+=1
print(r)