x, k, d = map(int, input().split())

def sgn(x):
  if x > 0:
    return 1
  if x < 0:
    return -1
  return 0

if x > 0:
  x1 = x - k * d
else:
  x1 = x + k * d

if sgn(x) == sgn(x1):
  print(abs(x1))
  exit()
  
xright = x % d
xleft = x % d - d
#0目前
xr = (abs(x - xright) // d) % 2
if k % 2 == xr:
  print(abs(xright))
elif k % 2 != xr:
  print(abs(xleft))