a,b,c = [int(x) for x in input().split()]
import math
si = math.sin(math.radians(c))
co = math.cos(math.radians(c))
s = a*b*si/2
l = a + b + (a**2 + b**2 - 2*a*b*co)**(1/2)
h = 2*s/a 
print("{:.6f}".format(s))
print("{:.6f}".format(l))
print("{:.6f}".format(h))

