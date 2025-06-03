def warshall_floyd(edge):
  e=edge
  for k in range(len(e)):
    for i in range(len(e)):
      for j in range(len(e)):
        e[i][j]=min(e[i][j],e[i][k]+e[k][j])
  return e

n,m,l=map(int,input().split())

edge=[n*[10**18]for _ in range(n)]
for i in range(n):
  edge[i][i]=0
for i in range(m):
  a,b,c=map(int,input().split())
  a-=1
  b-=1
  edge[a][b]=edge[b][a]=c
edge=warshall_floyd(edge)

edge2=[n*[10**18]for _ in range(n)]
for i in range(n):
  edge2[i][i]=0
  for j in range(n):
    if edge[i][j]<=l:
      edge2[i][j]=1

edge2=warshall_floyd(edge2)
q=int(input())
for i in range(q):
  s,t=map(int,input().split())
  s-=1
  t-=1
  ans=edge2[s][t]
  if ans==10**18:
    print(-1)
  else:
    print(ans-1)
