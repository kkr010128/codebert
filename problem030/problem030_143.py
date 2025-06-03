import math

a,b,C=list(map(int,input().split()))

C_radian=math.radians(C)

S=a*b*math.sin(C_radian)/2
L=a+b+(a**2+b**2-2*a*b*math.cos(C_radian))**0.5
h=b*math.sin(C_radian)

print(S)
print(L)
print(h)