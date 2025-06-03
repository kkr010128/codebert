import math
a = [int(s) for s in input().split()]
b = int(max([a[0], a[1]]))
c = int(min([a[0], a[1]]))
d = 0.5 * (a[2] * 60 + a[3])
e = 6 * a[3]
f = abs(d - int(e))

if f >= 180:
  f = 360 - f
if f != 0 and f!= 180:
  print(math.sqrt(a[0] ** 2 + a[1] ** 2 - 2 * a[0] * a[1] * math.cos(math.radians(f))))
elif f == 0:
  print(b-c)
else:
  print(b+c)