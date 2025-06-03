import math
a, b, x = map(int, input().split())
if 2 * x >= a * a * b: print(math.degrees(math.atan(2/a*(b-x/a** 2))))
else: print(math.degrees(math.atan(a*b*b/(2*x))))
