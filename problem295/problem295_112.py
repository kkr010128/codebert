import sys
I=sys.stdin.readlines()
N,M,L=map(int,I[0].split())
a,b,c=0,0,0
D=[[L+1]*N for i in range(N)]
for i in range(M):
  a,b,c=map(int,I[i+1].split())
  a,b=a-1,b-1
  D[a][b]=c
  D[b][a]=c
for i in range(N):
  D[i][i]=0
for k in range(N):
  for i in range(N):
    for j in range(N):
      D[i][j]=min(D[i][j],D[i][k]+D[k][j])
D2=[[N*N+2]*N for i in range(N)]
for i in range(N):
  D2[i][i]=0
  for j in range(N):
    if D[i][j]<=L:
      D2[i][j]=1
for k in range(N):
  for i in range(N):
    for j in range(N):
      D2[i][j]=min(D2[i][j],D2[i][k]+D2[k][j])
Q=int(I[M+1])
for i in range(Q):
  a,b=map(int,I[i+2+M].split())
  if N<D2[a-1][b-1]:
    print(-1)
  else:
    print(D2[a-1][b-1]-1)