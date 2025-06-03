n,m,x=map(int,input().split())
money=[]
skill=[]
for i in range(n):
  a=list(map(int,input().split()))
  money+=[a[0]]
  skill+=[a[1:m+1]]
ans=-1
for i in range(2**n):
  total=0
  learn=[0]*m
  for j in range(n):
    if (i>>j)&1:
      total+=money[j]
      for a in range(m):
        learn[a]+=skill[j][a]
  if len([i for i in learn if i>=x])==m:
    if ans==-1:
      ans=total
    elif ans>total:
      ans=total
print(ans)