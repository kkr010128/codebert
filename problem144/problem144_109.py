import math

a,b,h,m = map(int, input().split())

degree = abs(30*h+0.5*m) - (6*m)

if degree >= 180:
    degree = 360 - degree

radians = math.pi*degree/180
length = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(radians))
print(length)
