import math

a,b,x = list(map(int,input().split()))

theta = math.degrees(math.atan(a*b*b/2/x))

if(b/math.tan(math.radians(theta)) > a):
    theta = math.degrees(math.atan((2*a*a*b-2*x)/a/a/a))


print('{:.7f}'.format(theta))

