import math
n,k = map(int,input().split())
s = n//k
if n-k*s>abs(n-k*s-k):
  print(abs(n-k*s-k))
else:
  print(n-k*s)