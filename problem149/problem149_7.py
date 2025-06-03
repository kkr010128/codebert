n,m,x=map(int,input().split())
c=[]
a=[]
mn=float("inf")
for i in range(n):
  aa=list(map(int,input().split()))
  c.append(aa.pop(0))
  a.append(aa)

for i in range(2**n):
  buy=[]
  kai=[0]*m
  cost=0
  for j in range(n):
    if((i>>j)&1):
      buy.append(j)
  for j in buy:
    cost+=c[j]
    for k in range(m):
      kai[k]+=a[j][k]
  fl=True
  for j in range(m):
    if kai[j]<x:
      fl=False
      break
  if fl:
    mn=min(mn,cost)
if mn==float("inf"):
  print(-1)
else:
  print(mn)