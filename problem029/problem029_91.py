import math
x1, y1, x2, y2 = map(float, raw_input().split())
x, y = x2 - x1, y2 - y1
print math.sqrt(x**2 + y**2)