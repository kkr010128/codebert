import math

a, b, c = map(float, input().split())
h = b * math.sin(math.radians(c))
c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(c)))
L = a + b + c
S = 1 / 2 * a * h
print(S)
print(L)
print(h)
