#bit全探索

n,m,x=map(int,input().split())
c=[]
a=[]
for i in range(n):
  l=list(map(int,input().split()))
  c.append(l[0])
  a.append(l[1:])

min_cost=float('inf')
for i in range(2**n):
  flag=True
  cost_total=0
  a_total=[0]*m
  for j in range(n):
    if (i>>j)&1:
      cost_total+=c[j]
      for k in range(m):
        a_total[k]+=a[j][k]
  for s in range(m):
    if a_total[s]<x:flag=False
  if flag:
    min_cost=min(min_cost,cost_total)
  
if min_cost==float('inf'):
  print(-1)
else:
  print(min_cost)