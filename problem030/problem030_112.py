import math
a,b,agree=map(float,input().split())
agree=math.radians(agree)

c=(a**2+b**2-2*a*b*math.cos(agree))**0.5
s=0.5*a*b*math.sin(agree)
l=a+b+c
h=b*math.sin(agree)

print("{0:.5f}".format(s))
print("{0:.5f}".format(l))
print("{0:.5f}".format(h))
