import math
n,m,t = map(int,input().split())
if n%m == 0:
  print(int(n/m)*t)
else:
  print(math.ceil(n/m)*t)