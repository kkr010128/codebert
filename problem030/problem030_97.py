import math
a,b,C=map(float,input().split())
S=(a*b*math.sin(math.radians(C)))/2
c=a**2+b**2-2*a*b*math.cos(math.radians(C))
L=a+b+c**(1/2)

if C==90:
    h=b
else:
    h=(2*S)/a
    
print(f'{S:10.8f}')
print(f'{L:10.8f}')
print(f'{h:10.8f}')
