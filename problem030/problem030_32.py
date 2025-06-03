import math
a, b, c = map(float, input().split())
r = math.radians(c)
S = (a * b * math.sin(r)) / 2
print(S)
d = (a**2 + b**2 - 2 * a * b * math.cos(r))
d = math.sqrt(d)
L = a + b + d
print(L)
h = 2 * S / a
print(h)