import math
a,b,c = map(float,input().split())
H = b * math.sin(math.radians(c))
S = (a*(b*math.sin(math.radians(c))))/2
L = a + b + ((a**2) + (b**2) -(((2*a)*b)*math.cos(math.radians(c))))**0.5 
print(float(S))
print(float(L))
print(float(H))

