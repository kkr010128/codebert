import math 
a, b, h, m = map(int , input().split())
theta = abs( (h/12) + (m/60) * (1/12) - m/60)*2*math.pi


print(math.sqrt(b**2 * math.sin(theta)**2 + (b*math.cos(theta) -a) **2))