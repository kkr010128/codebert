import math
a,b,c=map(int, input().split())
c=math.radians(c)
print(0.5*a*b*math.sin(c))
print(a+b+math.sqrt(a**2+b**2-2*a*b*math.cos(c)))
print(b*math.sin(c))