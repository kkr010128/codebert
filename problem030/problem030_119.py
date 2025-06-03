import math
a,b,rad_c = map(int,input().split())
S = b * a * math.sin(math.pi / 180 * rad_c) / 2
c = math.sqrt(a**2 + b**2 -2 * a * b * math.cos(math.pi / 180 * rad_c))
L = a + b + c
h = b * math.sin(math.pi / 180 * rad_c)
print(S,L,h)