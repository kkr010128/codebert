from bisect import bisect
import math
n,k=map(int,input().split())
A=list(map(int,input().split()))


l,r = 0,max(A)

while l < r - 1:
  mid = (l+r)//2
  cnt = 0
  for a in A:
    cnt += math.ceil(a/mid) - 1
  #print(l,r,mid,cnt,k)
  if cnt <= k:
    r = mid
  else:
    l = mid
print(r)
