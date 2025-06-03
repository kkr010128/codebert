import math

a, b, x = map(float, input().split())
if a * a * b <= x * 2:
    h = 2 * (b - x / a / a)
    ret = math.degrees(math.atan2(h, a))
else:
    h = 2 * x / a / b
    ret = 90 - math.degrees(math.atan2(h, b))
print(ret)
