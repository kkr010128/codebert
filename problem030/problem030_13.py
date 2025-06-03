import math
a, b, c = map(int, input().split())

c = math.radians(c)
s = a * b * math.sin(c) / 2
d = math.sqrt(a**2 + b**2 - 2*(a * b * math.cos(c)))
h = b * math.sin(c)

for i in (s, a+b+d, h):
    print(i)
