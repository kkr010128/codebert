import math

a, b, C = map(int, input().split())
rad_C = math.radians(C)
c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(rad_C))
h = b * math.sin(rad_C)
L = a + b + c
s = a * h / 2
print(s)
print(L)
print(h)