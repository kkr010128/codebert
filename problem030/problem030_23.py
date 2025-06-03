import math
a, b, C=map(int, input().split())
print("{0:.5f}".format((1/2)*a*b*math.sin(C*math.pi/180.0)))
print("{0:.5f}".format(a+b+math.sqrt(a**2+b**2-2*a*b*math.cos(C*math.pi/180))))
print("{0:.5f}".format(b*math.sin(C*math.pi/180.0)))