import math
a, b, deg = map(int, input().split())
rad = math.radians(deg)

S = a * b * math.sin(rad) / 2
c = (a ** 2 + b ** 2 - 2 * a * b * math.cos(rad)) ** (1 / 2)
L = a + b + c
h = S * 2 / a

print(S,L,h)
