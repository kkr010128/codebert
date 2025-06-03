import math
n,k=map(int,input().split())
a=list(map(int,input().split()))

def is_ok(arg):
  cnt=0
  for i in a:
    cnt+=(i-1)//arg
  return k>=cnt
  
def binsearch(ng,ok):
  while abs(ok-ng)>1:
    mid=(ok+ng)//2
    if is_ok(mid):
      ok=mid
    else:
      ng=mid
      
  return ok

print(binsearch(0,10**9+1))