import math
a,b,C = map(float,input().split())
rad = math.radians(C)
h = b*math.sin(rad)
S = a*h/2
L = a+b+math.sqrt(a**2+b**2-2*a*b*math.cos(rad))

print("%.5f\n%.5f\n%.5f" % (S,L,h))