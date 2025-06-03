import math
a,b,C=map(int,input().split())


c=C/180*math.pi
d=math.sqrt(a**2+b**2-2*a*b*math.cos(c))
S=1/2*a*b*math.sin(c)
L=a+b+d
h=2*S/a

print("{:.8f}".format(S))
print("{:.8f}".format(L))
print("{:.8f}".format(h))


