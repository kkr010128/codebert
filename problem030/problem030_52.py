import math
a,b,c = map(float,input().split())
rad = math.radians(c)
x = (a**2+b**2-2*a*b*math.cos(rad))**(1/2)
L = a+b+x
S = a*b*math.sin(rad)/2
h = 2*S/a
print("{:.8f}\n{:.8f}\n{:.8f}".format(S,L,h))
