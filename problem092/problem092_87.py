x, k, d = [int(i) for i in input().split()]
if x < 0:
  x = -x
l = min(k, x // d)
k -= l
x -= l * d
if k % 2 == 0:
  print(x)
else:
  print(d - x)