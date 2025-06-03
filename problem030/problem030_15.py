import math
a,b,x=map(float, input().split())
h=b*math.sin(math.pi*x/180)
c=(a**2+b**2-2*a*b*math.cos(math.pi*x/180))**0.5
print(a*h*0.5)
print(a+b+c)
print(h)