import math
a,b,c,d = (int(x) for x in input().split())
if math.ceil (a/d) < math.ceil (c/b):
  print ('No')
else:
  print ('Yes')