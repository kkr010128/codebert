import math
x1, y1, x2, y2 = map(float, input().split())
x = math.fabs(x2 - x1)
y = math.fabs(y2 - y1)
d = math.sqrt(x**2 + y**2)
print('{:.8f}'.format(d))

