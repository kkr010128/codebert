import math
a, b, C = map(int, input().split())
rad = C/180*math.pi
print('%.8f' % (a*b*math.sin(rad)/2))
print('%.8f' % ((a**2-2*a*b*math.cos(rad)+b**2)**0.5 + a + b))
print('%.8f' % (b * math.sin(C/180*math.pi)))
