import math
a, b, x = map(int, input().split())

if x < a ** 2 * b / 2:
    theta = math.atan2(b, 2 * x / b / a)
else:
    theta = math.atan2(2 * b - 2 * x / a / a, a)
deg = math.degrees(theta)
print(deg)

