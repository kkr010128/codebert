import math
a,b,h,m=map(int,input().split())
print((a**2+b**2-2*a*b*math.cos(math.pi*(m*11/360-h/6)))**0.5)