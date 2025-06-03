import math
a, b, C = map(int, input().split())
C = math.radians(C)
S = a * b * math.sin(C) * 0.5
c = math.sqrt(a * a + b * b - 2 * a * b * math.cos(C))
L = a + b + c
h = 2 * S / a
print(S, L, h)
