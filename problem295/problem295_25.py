import sys
input=sys.stdin.readline
N,M,L=map(int,input().split())

def warshall_floyd(d):
  #d[i][j]: iからjへの最短距離
  for k in range(size_v):
    for i in range(size_v):
      for j in range(size_v):
        d[i][j]=min(d[i][j],d[i][k]+d[k][j])
  return d

# vlistに点のリスト、dist[vi][vj]に辺(vi,vj)のコストを入れて呼び出す
size_v=N+1
dist=[[float("inf")]*size_v for i in range(size_v)]
for _ in range(M):
  A,B,C=map(int,input().split())
  dist[A][B]=C
  dist[B][A]=C
for i in range(size_v):
  dist[i][i]=0 #自身のところに行くコストは0

dist=warshall_floyd(dist)
#print(dist)

dist2=[[float("inf")]*size_v for i in range(size_v)]
for i in range(size_v):
  for j in range(size_v):
    if dist[i][j]<=L:
      dist2[i][j]=1
for i in range(size_v):
  dist2[i][i]=0 #自身のところに行くコストは0

dist2=warshall_floyd(dist2)
#print(dist2)

Q=int(input())
for _ in range(Q):
  s,t=map(int,input().split())
  answer=dist2[s][t]-1
  if answer==float("inf"):
    print(-1)
  else:
    print(answer)