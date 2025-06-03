n,k=map(int,input().split())
a=list(map(int,input().split()))
l=0;r=10**10
while r-l>1:
  x=(l+r)//2
  ct=0
  for i in range(n):
    ct+=(a[i]-1)//x
  if ct<=k:
    r=x
  else:
    l=x
print(r)