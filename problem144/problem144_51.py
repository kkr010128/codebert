import math
a, b, h, m = map(int, input().split())
c = abs((60*h+m)*0.5 - m*6)
if c>180:
    c=360-c
c=(a**2 + b**2 - 2*a*b*math.cos(math.radians(c)))**0.5
print(c)