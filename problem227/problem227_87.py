import sys
n,k=map(int,input().split())
h=list(map(int,input().split()))

if n<=k:
  print(0)
  sys.exit()

hi=sorted(h)
if k:
  print(sum(hi[:-k]))
else:
  print(sum(hi))
