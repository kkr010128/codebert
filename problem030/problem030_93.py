import math

a, b, C = map(float, input().split())
S = (a * b * math.sin(math.radians(C))) / 2
L = a + b + (a**2 + b**2 - 2 * a * b * math.cos(math.radians(C)))**0.5
h = b * math.sin(math.radians(C))
print(S)
print(L)
print(h)
