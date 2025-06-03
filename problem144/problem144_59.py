import math
a, b,h,m = list(map(int, input().split()))
rel_hour = (h*60 + m)/12/60
#print(rel_hour)
arg_hour = 2* math.pi *rel_hour
arg_min = 2*math.pi * m/60
ans = (abs(a**2+b**2-2*a*b*math.cos(arg_hour-arg_min)))**(1/2)
print(ans)