import math

a, b, C = map(int, input().split())

h = b * math.sin(math.radians(C))
S = a * h * 0.5
L = a + b + math.sqrt(pow(a, 2) + pow(b, 2) - 2 * a * b *math.cos(math.radians(C)))

print(S)
print(L)
print(h)