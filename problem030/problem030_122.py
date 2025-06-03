import math
a,b,c=map(float,input().split())
c*=math.pi/180
print(.5*a*b*math.sin(c))
print(a+b+math.sqrt(a*a+b*b-2*a*b*math.cos(c)))
print(b*math.sin(c))
