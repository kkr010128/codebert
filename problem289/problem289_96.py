import math
a, b, x = map(int, input().split())
if x >= a**2 * b / 2:
    tan = (2 * (a ** 2 * b - x)) / a ** 3
else:
    tan = (a*b**2) / (2 * x)
print(math.atan(tan)/ math.pi * 180)
