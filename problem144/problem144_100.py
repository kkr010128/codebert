A,B,H,M=map(int, input().split())
import math

angle = abs(30*H-5.5*M)
angle = min(angle, 360-angle)*math.pi/180
 
c=A**2 + B**2 -2*A*B* math.cos(angle)
c=c**0.5
 
print(c)