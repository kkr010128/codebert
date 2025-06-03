import math
x1, y1, x2, y2 = map(float,input().split())
a = abs(x1-x2)
b = abs(y1-y2)

print(math.sqrt(a*a+b*b))
