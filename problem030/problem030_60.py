import math
a,b,C=map(float,input().split())

S = a*b*math.sin(C*math.pi/180)/2
c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(C*math.pi/180))
h = 2*S/a
print("{:10f}".format(S))
print("{:10f}".format(a+b+c))
print("{:10f}".format(h))

