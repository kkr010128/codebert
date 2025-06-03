import math
e=map(float,raw_input().split())
a=e[0]
b=e[1]
C=math.radians(e[2])
c=(a**2+b**2-2*a*b*math.cos(C))**0.5
h=b*math.sin(C)
S=h*a*0.5
L=a+b+c
print S
print L
print h
