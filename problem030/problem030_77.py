import math
a,b,c=map(float,input().split())
c=math.radians(c)
h=b*math.sin(c)
s=a*h/2
d=math.sqrt(a**2+b**2-2*a*b*math.cos(c))
l=a+b+d
print(s,l,h)