import math

x1, y1, x2, y2 = map(float, input().split())

dx = x1 - x2
dy = y1 - y2

d = math.hypot(dx, dy)

print(d)