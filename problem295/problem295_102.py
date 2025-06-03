def W(d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

##############################
n,w,l= map(int,input().split()) #n:頂点数　w:辺の数

d = [[10**14]*n for i in range(n)] 
#d[u][v] : 辺uvのコスト(存在しないときはinf)
for i in range(w):
    x,y,z = map(int,input().split())
    if z>l:
      continue
    x=x-1
    y=y-1
    d[x][y] = z
    d[y][x] = z
for i in range(n):
    d[i][i] = 0 #自身のところに行くコストは０
D=W(d)
G=[[10**4]*n for i in range(n)]
for i in range(n):
  for j in range(n):
    if D[i][j]>l:
      continue
    G[i][j]=1
WW=W(G)
for i in range(int(input())):
  a,b=map(int,input().split())
  a=a-1
  b=b-1
  if WW[a][b]>=10**4:
    print(-1)
  else:
    print(WW[a][b]-1)