import math
A,B,N = map(int,input().split())
ret = 0
ans = 0
if B == 0:
  print(0)
  exit()
if B > N:
  base = N
else:
  base = B - 1
ret = math.floor(A*base/B) - A*math.floor(base/B)
print(ret)