from math import *
a, b, C = map(float, input().split())
c = sqrt(a ** 2 + b ** 2 - 2 * a * b * cos(radians(C)))
s = (a + b + c) / 2
S = sqrt(s * (s - a) * (s - b) * (s - c))
L = a + b + c
h = b * sin(radians(C))
print(S)
print(L)
print(h)

