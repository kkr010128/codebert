# ITP1_10_B
import math

a, b, c = map(float, input().split())
s = a * b * math.sin(math.radians(c)) / 2
l = a + b + math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(math.radians(c)))
h = b * math.sin(math.radians(c))

print(s)
print(l)
print(h)

