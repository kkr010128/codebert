import math

a,b,h,m = map(int, input().split())

xh = a*math.cos((60*h+m)/360*math.pi)
yh = a*math.sin((60*h+m)/360*math.pi)

xm = b*math.cos(m/30*math.pi)
ym = b*math.sin(m/30*math.pi)

print( ((xh-xm)**2+(yh-ym)**2)**0.5 )