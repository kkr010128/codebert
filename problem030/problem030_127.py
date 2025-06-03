import math
a,b,C = map(float,input().split())
S = 1/2*a*b*math.sin(C*math.pi/180)
c = math.sqrt(a**2+b**2-2*a*b*math.cos(C*math.pi/180))
L = a+b+c
h = 2*S/a
print(format(S,'.8f'))
print(format(L,'.8f'))
print(format(h,'.8f'))
