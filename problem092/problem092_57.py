import math
x,k,d = map(int,input().split())
d = abs(d)
x = abs(x)

if k*d<=x:
  print(x-k*d)
else:
  e = math.floor(x/d)
  k -= e
  x = x-e*d
  if k%2 == 0:
    print(x)
  else:
    print(abs(x-d))

