import math
a,b,c = map(float, input().split())

r = c * (math.pi/180)
h = b * math.sin(r)
S = 0.5 * a * b * math.sin(r)
L = a + b + math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(r))
print(S)
print(L)
print(h)

