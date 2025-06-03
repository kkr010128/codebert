import math

a,b,c = map(float,input().split())

sinc = math.sin(c*math.pi/180)
cosc = math.cos(c*math.pi/180)
c = math.sqrt(a**2+b**2-2*a*b*cosc)
s = a*b*sinc/2.0

print(s)
print(a+b+c)
print(s/a*2.0)
