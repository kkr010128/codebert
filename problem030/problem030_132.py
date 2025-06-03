import math

a,b,C=map(int,input().split())
C2=math.radians(C)
sin=math.sin(C2)
cos=math.cos(C2)
S = 0.5*a*b*sin
L = a+b+(math.sqrt((a**2+b**2)-(2*a*b*cos)))
H = (a*b*sin/2)/(a/2)
print("{0:.8f}".format(S))
print("{0:.8f}".format(L))
print("{0:.8f}".format(H))