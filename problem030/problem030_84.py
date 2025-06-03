a,b,c=list(map(float,input().split()))
import math
print(math.sin((2*c*math.pi)/360)*a*b*(1/2))
print(math.sqrt(a**2+b**2-2*a*b*math.cos(2*c*math.pi/360))+a+b)
print(math.sin(2*c*math.pi/360)*b)