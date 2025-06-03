import itertools
n,m,x=map(int,input().split())
lst=[list(map(int,input().split())) for i in range(n)]
ans=10**7
for buy in itertools.product(range(2),repeat=n):
  judge=[0]*(m+1)
  for i in range(n):
    if buy[i]==1:
      for j in range(m+1):
        judge[j]+=lst[i][j]
  jd=True
  for i in range(1,m+1):
    if judge[i]<x:
      jd=False
      break
  if jd:
    ans=min(ans,judge[0])
if ans==10**7:
  ans=-1
print(ans)