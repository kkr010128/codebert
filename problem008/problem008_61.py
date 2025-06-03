def d(u):
 global t
 C[u]=1;t+=1;D[u]=t
 for v in range(N):
  if M[u][v]and C[v]==0:d(v)
 C[u]=2;t+=1;F[u]=t
N=int(input())
M=[[0]*N for _ in[0]*N]
for e in[list(map(int,input().split()))for _ in[0]*N]:
 for v in e[2:]:M[e[0]-1][v-1]=1
C,D,F=[0]*N,[0]*N,[0]*N
t=0
for i in range(N):
 if C[i]==0:d(i)
for i in range(N):print(i+1,D[i],F[i])
