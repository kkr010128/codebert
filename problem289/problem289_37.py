a, b, x = map(int, input().split())

if x >= a**2*b/2:
    t = 2*(b*a**2-x)/(a**3)
else:
    t = (a*b**2)/(2*x)

import math
p = math.atan(t)
p = math.degrees(p)
print(p)
