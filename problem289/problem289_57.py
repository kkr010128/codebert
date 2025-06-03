a, b, x = map(int, input().split())

import math

if a**2 * b < 2 * x:
    tangent = (2 * (a**2 * b - x)) / a ** 3
    theta = math.degrees(math.atan(tangent))
    print(theta)
else:
    tangent = (a * b**2) / (2 * x)
    theta = math.degrees(math.atan(tangent))
    print(theta)