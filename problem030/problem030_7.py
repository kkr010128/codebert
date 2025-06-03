from math import *
a, b, C = (int(i) for i in input().split())
C = pi * C / 180
c = sqrt(a**2 + b**2 - 2 * a * b * cos(C))

h = b * sin(C)
S = a * h / 2
L = a + b + c
print("{:.8f} {:.8f} {:.8f}".format(S, L, h))