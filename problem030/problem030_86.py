import math

a, b, c = map(float,input().split())
e = b*math.sin(math.radians(c))
print(a*e/2)
print(((a-b*math.cos(math.radians(c)))**2+e**2)**0.5+a+b)
print(e)

