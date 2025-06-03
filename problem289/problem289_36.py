a,b,x=map(int,input().split())
import math
v=a*a*b
if x>=v/2:
    print(180*math.atan(2*(v-x)/(a*a*a))/math.pi)
else:
    print(90-(180*math.atan(2*x/(a*b*b)))/math.pi)