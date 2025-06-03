import math
a,b,h,m = map(int, input().split())
s = 30 * h + m * 0.5
l = m*6
x = abs(s-l)
if x >= 180: x = 360-x
c = math.cos(math.radians(x))
print((a**2+b**2-2*a*b*c)**0.5)