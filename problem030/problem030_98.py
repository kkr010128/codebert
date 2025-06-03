import math
a, b, C=map(int,input().split())
S=a*b*math.sin(math.pi*C/180)/2
c=math.sqrt(a**2+b**2-2*a*b*math.cos(math.pi*C/180))
L=a+b+c
h=2*S/a
print('{:.4f}'.format(S))
print('{:.4f}'.format(L))
print('{:.4f}'.format(h))
