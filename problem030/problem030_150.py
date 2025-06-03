a,b,c=map(int,input().split())
import math
d=math.radians(c)
S=a*b*math.sin(d)*(1/2)
e=math.cos(d)
x=a**2+b**2-2*a*b*e
L=a+b+math.sqrt(x)
h=2*S/a

print('{:.6f}'.format(S))
print('{:.6f}'.format(L))
print('{:.6f}'.format(h))
