import math
a,b,x = map(int,input().split())

if x >= 0.5 * a**2 * b:
    tan_x = 2*(b*a**2 -x)/a**3

else:
    tan_x = (b**2 * a)/(2*x)

print(math.degrees(math.atan(tan_x)))
