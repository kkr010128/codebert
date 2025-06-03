import math
a,b,x = map(int,input().split())

if x <= a*a*b//2:
    theta = (math.pi/2) - math.atan((2*x)/(a*b*b))
else:
    theta = math.atan(2*(a*a*b-x)/(a*a*a))

degree = math.degrees(theta)
print(degree)