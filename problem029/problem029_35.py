from math import sqrt
x1, y1, x2, y2 = map(float, input().split())
X = abs(x1 - x2)
Y = abs(y1 - y2)
print(sqrt(X**2 + Y**2))
