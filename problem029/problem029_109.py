import math
x1, y1, x2, y2 = map(float, input().split())
x = x2 - x1
y = y2 - y1

result = x**2 + y**2
print(math.sqrt(result))