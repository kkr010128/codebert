import math
a,b,c=map(float,input().split())
C=math.radians(c)
D=math.sin(C)*a*b
S=D/2
E=a**2+b**2-2*a*b*math.cos(C)
F=math.sqrt(E)
L=a+b+F
if C<90:
    h=b*math.sin(C)
elif C==90:
    h=b
else:
    h=b*math.sin(180-C)
print(S,L,h)
