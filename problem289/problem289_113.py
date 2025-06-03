from math import atan,pi
a,b,x=map(int,input().split())
if a*a*b/2<=x:
    h=x/(a**2)
    c=(b-h)*2
    theta=atan(c/a)/2/pi*360
    print(theta)
else:
    c=2*x/b/a
    theta=atan(b/c)/2/pi*360
    print(theta)
