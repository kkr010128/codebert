import math
a, b, C = map(int, input().split())
C = math.radians(C)
S, h = (1/2)*a*b*math.sin(C), b*math.sin(C)
L = a+b+math.sqrt((a**2)+(b**2)-(2*a*b*math.cos(C)))
print("{0:.8f}".format(S))
print("{0:.8f}".format(L))
print("{0:.8f}".format(h))