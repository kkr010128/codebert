import math
a,b,C = map(int, input().split())
r = C*math.pi/180
h = b*math.sin(r)
print('{0:f}'.format(a*h/2))
print('{0:f}'.format(a+b+(math.sqrt(a**2+b**2-2*a*b*math.cos(r)))))
print('{0:f}'.format(h))