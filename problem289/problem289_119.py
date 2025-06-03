from math import atan, pi
a,b,x = map(int,input().split())
h = x/(a**2)
if 2*h-b >= 0:
    print(atan((2*b-2*h)/a)*180/pi)
else:
    print(atan((b**2)/(2*h*a))*180/pi)