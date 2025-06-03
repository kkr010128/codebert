import math
a,b,c = [int(x) for x in input().split()]
c = math.radians(c)
s = a * b * math.sin(c) / 2
l = a + b + math.sqrt(a**2 + b**2 - 2*a*b*math.cos(c))
h = 2 * s / a
for i in [s,l,h]:
    print('{:.12f}'.format(i))

