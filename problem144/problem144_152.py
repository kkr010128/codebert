a,b,h,m = map(int,input().split())

a_y = ((h/12)*360+m/(60*12)*360)%360
b_y = ((m/60)*360)%360

from math import *

alpha = ((a_y - b_y)%360)*pi/180

ans = sqrt(a**2+b**2-2*a*b*cos(alpha))

print(ans)