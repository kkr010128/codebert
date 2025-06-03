import math

a, b, x = map(int, input().split())
x /= a
if a * b >= x * 2:
    c = x * 2 / b
    print(math.degrees(math.atan2(b, c)))
else:
    c = (a * b - x) * 2 / a
    print(math.degrees(math.atan2(c, a)))