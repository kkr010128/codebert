from math import sin, cos, radians, sqrt
a, b, C = map(float, input().split())
rad = radians(C)
h = b * sin(rad)
print(a * h / 2)
print(a + b + sqrt(a ** 2 + b ** 2 - 2 * a * b * cos(rad)))
print(h)
