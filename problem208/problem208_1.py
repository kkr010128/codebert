n,m=map(int, input().split())
alist=[list(map(int, input().split())) for i in range(m)]
ans=-1
for i in range(999,-1,-1):
  if len(str(i))==n:
    x=True
    stri=str(i)
    for j in range(m):
      if stri[alist[j][0]-1]!=str(alist[j][1]):
        x=False
    if x:
      ans=i
print(ans)