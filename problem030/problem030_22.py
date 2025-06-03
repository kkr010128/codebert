import math
a,b,c=map(float,input().split())
h=b*math.sin(c/180.0*math.pi)
ad=a-b*math.cos(c/180.0*math.pi)
d=(h*h+ad*ad)**0.5
l = a + b + d
s = a * h / 2.0
print('{0:.6f}'.format(s))
print('{0:.6f}'.format(l))
print('{0:.6f}'.format(h))