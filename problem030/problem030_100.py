import math
a, b, c = map(int, input().split())
c = math.radians(c)
S = 1 / 2 * (a * b * math.sin(c))
c2 = math.sqrt(a*a + b*b - 2*a*b*math.cos(c))
H = a + b + c2
h = b * math.sin(c)
print(S,H,h)

