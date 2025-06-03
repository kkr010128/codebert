import math
a, b, x = map(int, input().split())
theta = math.atan((-2) * x / (a ** 3) + 2 * b / a)
if a * math.tan(theta) > b:
    theta = math.atan2(a * b * b, 2 * x)
print(math.degrees(theta))