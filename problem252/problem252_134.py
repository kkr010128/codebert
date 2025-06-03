n,m=map(int,input().split())
A=[int(i) for i in input().split()]
A.sort()
s=sum(A)
SA=[0]
for a in A:
  SA.append(SA[-1]+a)
for i in range(n+1):
  SA[i]=s-SA[i]
l,r=0,2*max(A)+1
import bisect
def chk(x):
  ct=0
  for a in A:
    ct+=n-bisect.bisect_left(A,max(x-a,0))
  if ct>=m:
    return True
  else:
    return False

def count(x):
  ct=0
  for a in A:
    ct+=n-bisect.bisect_left(A,max(x-a,0))
  return ct

while r-l>1:
  mid=(l+r)//2
  if chk(mid):
    l=mid
  else:
    r=mid
ans=0
for a in A:
  aa=bisect.bisect_left(A,max(l-a,0))
  ans+=SA[aa]+a*(n-aa)
print(ans-l*(count(l)-m))
