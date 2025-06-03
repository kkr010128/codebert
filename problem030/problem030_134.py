from math import radians, sin, cos, sqrt
a, b, C = map(float, input().split())
h = b * sin(radians(C))
c = sqrt(a*a+b*b-2*a*b*cos(radians(C)))
S = a * h / 2
L = a + b + c
print(S, L, h)
