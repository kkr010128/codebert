import math
A, B, X = map(int, input().split())
h = X / (A*A)
r = 0
deg = 0
if (2 * X) - (B * A * A) > 0:
  r = math.atan(2 * (B-h) / A)
elif (2 * X) - (B * A * A) == 0:
  r = math.atan(B / A)
else:
  h = (2 * X) / (A * B)
  r = math.atan(B / h)
deg = math.degrees(r)
print(deg)