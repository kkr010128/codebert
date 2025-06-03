import math
a,b,C = (float(i) for i in input().split())
rad =math.radians(C)
S = a*b*0.5*math.sin(rad)
L = a+b+math.sqrt(a**2+b**2-2*a*b*math.cos(rad))
H = b*math.sin(rad)
print(S)
print(L)
print(H)