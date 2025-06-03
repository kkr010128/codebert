import math
A,B,H,M = map(int,input().split())
V1 = 30
V2 = 30/60
v = 6
d = abs( (V1*H + V2*M) - v*M)
if d == 0:
  print(abs(A-B))
else:
  print(math.sqrt(A**2 + B**2 -2*A*B*math.cos(math.radians(d))))