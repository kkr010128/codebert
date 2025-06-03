import math

a,b,C = tuple(float(n) for n in input().split())
C = math.radians(C)
S = a*b*math.sin(C) / 2
L = a + b + math.sqrt(a**2+b**2-2*a*b*math.cos(C))
h = b*math.sin(C)
print("{:.8f}\n{:.8f}\n{:.8f}".format(S,L,h))
