n,m=map(int, input().split())
alist=[list(map(int, input().split())) for i in range(m)]
ans=-1
if n==1:
  for i in range(9,-1,-1):
    x=True
    stri=str(i)
    for j in range(m):
      if stri[alist[j][0]-1]!=str(alist[j][1]):
        x=False
    if x:
      ans=i
else:
  for i in range(10**n-1,10**(n-1)-1,-1):
    x=True
    stri=str(i)
    for j in range(m):
      if stri[alist[j][0]-1]!=str(alist[j][1]):
        x=False
    if x:
      ans=i
print(ans)