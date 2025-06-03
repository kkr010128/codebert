import math

a, b, c = [float(line) for line in input().split()]
S = 1 / 2 * a * b * math.sin(math.radians(c))
c = math.sqrt((a ** 2) + (b ** 2) - (2 * a * b * math.cos(math.radians(c))))
L = a + b + c
H = S / (a * (1 / 2))

print(S, L, H)

