import math

point = map(float, raw_input().split())
x1 = point[0]
y1 = point[1]
x2 = point[2]
y2 = point[3]

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print distance