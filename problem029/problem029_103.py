import math

x1, y1, x2, y2 = map(float, input().split())
line = (x2 - x1) ** 2 + (y2 - y1) ** 2
line = math.sqrt(line)
print(line)

