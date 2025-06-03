n,k=map(int,input().split())
a=list(map(int,input().split()))
data=[0]*(n+1)
data[1]=1
ans=[1]
res=0
for i in range(n):
  p=a[res]
  if data[p]==0:
    data[p]=1
    ans.append(p)
    res=p-1
  else:
    res=ans.index(p)
    break
if len(ans)>k:
  print(ans[k])
else:
  m=len(ans)-res
  k-=res
  d=k%m
  print(ans[res+d])