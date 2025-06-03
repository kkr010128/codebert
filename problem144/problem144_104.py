import math
a,b,h,m = map(int,input().split())

h_s = 360*h/12+30*m/60
m_s = 360*m/60
s = abs(h_s - m_s)
print(abs(math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(s)))))