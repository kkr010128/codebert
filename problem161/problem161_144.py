a,b,n=map(int,input().split())

import math
if n/b >= 1:
  print(math.floor(a*(b-1)/b))
else:
  print(math.floor(a*n/b))