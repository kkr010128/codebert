import math
a,b,h,m=map(int, input().split())
a_x=math.cos(abs(math.radians(6*m)-math.radians(30*h+0.5*m)))
print((a**2+b**2-2*a*b*a_x)**0.5)
