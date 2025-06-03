N,M,Q=map(int,input().split())
Query=[list(map(int,input().split())) for i in range(Q)]
import itertools
ans=0
for x in itertools.combinations_with_replacement(range(1, M+1), N):
  l=0
  for i in range(Q):
    a,b,c,d=map(int,Query[i])
    if x[b-1]-x[a-1]==c:
      l+=d
  ans=max(ans,l)
print(ans)