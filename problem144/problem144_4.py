import math
a,b,h,m=map(int,input().split())
deg_a=6*m
deg_b=30*h+m/2
deg_c=abs((deg_a)-(deg_b))
rad=math.radians(deg_c)
c=a**2+b**2-2*a*b*math.cos(rad)
print(c**0.5)
