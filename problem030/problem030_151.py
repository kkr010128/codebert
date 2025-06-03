import math
a, b, C = map(float, input().split())
C = C / 180 * math.pi
print('%.06f' % (a * b * math.sin(C) / 2))
print('%.06f' % ((a**2 + b**2 -2*a*b*math.cos(C))**(1/2) + a + b))
print('%.06f' % (b*math.sin(C)))