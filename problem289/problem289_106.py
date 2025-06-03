import math
a,b,x = map(int,input().split())
if x > a*a*b/2:
    tan = 2*(a*a*b - x)/(a*a*a)
elif x <= a*a*b/2:
    tan = a*b*b/(2*x)
print(math.degrees(math.atan(tan)))