import math
a,b,C=map(float,input().split())
print(f'{a*b/2*math.sin(math.radians(C)):.6f}')
print(f'{a+b+(a**2+b**2-2*a*b*math.cos(math.radians(C)))**0.5:.6f}')
print(f'{b*math.sin(math.radians(C)):.6f}')
