import math
a,b,x=map(int,input().split())

if x>=a**2*b/2:
    a=math.atan((2/a)*(b-x/(a**2)))
else:
    a=math.atan(a*b**2/2/x)

print("{:.8f}".format(a*(180/math.pi)))