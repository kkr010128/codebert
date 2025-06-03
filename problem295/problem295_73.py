N,M,L=map(int, input().split())
def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j]=min(d[i][j],d[i][k] + d[k][j])
    return d

d=[[float("inf")]*N for i in range(N)] 
#d[u][v] : 辺uvのコスト(存在しないときはinf)
for i in range(M):
    x,y,z=map(int,input().split())
    d[x-1][y-1]=z
    d[y-1][x-1]=z
for i in range(N):
    d[i][i]=0 #自身のところに行くコストは０
D=warshall_floyd(d)
E=[[float("inf")]*N for i in range(N)] 
for i in range(N):
  for j in range(N):
    if D[i][j]==0:
      E[i][j]=0
    elif D[i][j]<=L:
      E[i][j]=1
F=warshall_floyd(E)
N=int(input())
for i in range(N):
  x,y=map(int,input().split())
  if F[x-1][y-1]==float("inf"):
    print(-1)
  else:
    print(F[x-1][y-1]-1)