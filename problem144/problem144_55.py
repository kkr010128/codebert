import math
 
A,B,H,M = map(int,input().split())
 
degree = 0
minute = 6*M
hour=30*H+0.5*M
if abs(minute-hour)>=180:
  degree = 360-abs(minute-hour)
else :
  degree = abs(minute-hour)
#print (degree)
#print (math.degrees(degree))
#print (math.cos(math.radians(degree)))
 
c=A**2+B**2-2*A*B*math.cos(math.radians(degree))
print (math.sqrt(c))