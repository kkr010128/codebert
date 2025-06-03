a,b,c,k=[int(x) for x in input().split()]
ans=0
if a<=k:
  ans+=a
  k-=a
elif k>0:
  ans+=k
  k=0
if b<=k:
  k-=b
elif k>0:
  k=0
if k>0:
  ans-=k
print(ans)