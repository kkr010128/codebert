n,k=map(int,input().split())
h=list(map(int,input().split()))
if n<=k:
  print(0)
  exit()
h.sort()
if k==0:
  print(sum(h))
else:
  print(sum(h[:-k]))