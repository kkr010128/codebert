n,*a=map(int,open(0).read().split())
a.sort()
num=[True for i in range(a[-1]+1)]
for i in range(n):
  if num[a[i]]:
    for j in range(a[-1]//a[i]+1):
      if j<2:
        continue
      num[a[i]*j]=False
    if i==n-1:
      pass
    elif a[i]==a[i+1]:
      num[a[i]]=False
    else:
      pass
  else:
    continue
ans=0
for i in range(n):
  if num[a[i]]:
    ans+=1
print(ans)