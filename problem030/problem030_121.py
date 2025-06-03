import math

a,b,c_deg = map(float,input().split())

sin_c = math.sin(c_deg*math.pi/180)
cos_c = math.cos(c_deg*math.pi/180)

s = a*b*sin_c/2.0
c = math.sqrt(a**2+b**2-2*a*b*cos_c)

print(s)
print(a+b+c)
print(s/a*2.0)