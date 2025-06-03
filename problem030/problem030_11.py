import math
a, b, c = map(float, input().split())
s = a*b*math.sin(math.radians(c))/2
h = 2*s/a
l = a + b + (a**2+b**2 - 2*a*b*math.cos(math.radians(c)))**0.5
print("{0:.5f} {1:.5f} {2:.5f}".format(s,l,h))