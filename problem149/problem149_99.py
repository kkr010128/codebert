from itertools import product as prod
N,M,X=map(int,input().split())
B=[list(map(int,input().split())) for _ in range(N)]
ans=float('INF')
for v in prod(range(2),repeat=N):
  scores=[0]*M
  cost=0
  for i in range(N):
    if v[i]==1:
      cost+=B[i][0]
      for j in range(M):
        scores[j]+=B[i][1+j]
  if min(scores)>=X:
    ans=min(ans,cost)

print(ans if ans!=float('INF') else -1)