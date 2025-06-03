import math

a, b, c = map(float, input().split())
c = math.radians(c)

S = 0.5 * a * b * math.sin(c)
L = (a ** 2 + b ** 2 - 2 * a * b * math.cos(c)) ** 0.5 + a + b
h = S / a * 2

print(S)
print(L)
print(h)