a,b,h,w=map(int,input().split())
import math
theta=math.radians(abs((h+w/60)*360/12-w*360/60))

c=(a**2+b**2-2*a*b*math.cos(theta))**0.5
print(c)