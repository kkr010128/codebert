import math
a,b,C = map(int,input().split())
C = math.radians(C)
c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(C))
S = 1/2*a*b*math.sin(C)
L = a+b+c
h = b * math.sin(C)
print('{0:.5f}\n{1:.5f}\n{2:.5f}'.format(S,L,h))

