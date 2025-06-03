from collections import deque
n=int(input())
edge=[[] for _ in range(n+1)]
for i in range(n):
  v,k,*u=map(int,input().split())
  edge[v]=u
p=[-1]*(n+1)
p[1]=0
q=deque([])
q.append(1)
v=[1]*(n+1)
v[1]=0
while q:
  now=q.popleft()
  for i in edge[now]:
    if v[i]:
      q.append(i)
      p[i]=p[now]+1
      v[i]=0
for i in range(1,n+1):
  print(i,p[i])
