from math import sin, cos, radians

a, b, C = (float(x) for x in input().split())
s = a * b * sin(radians(C)) * 0.5
l = (a **2 + b**2 - 2 * a * b * cos(radians(C))) ** 0.5 + a + b
h = s * 2 / a
print(s)
print(l)
print(h)