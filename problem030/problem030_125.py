import math
a, b, C = map(int, input().split())
C = C / 180 * math.pi
S = a * b * math.sin(C) / 2
print(S)
print(a + b + math.sqrt(a**2 + b**2 - 2*a*b*math.cos(C)))
print(2 * S / a)