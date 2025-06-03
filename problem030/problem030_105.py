import math

a, b, C = map(int, input().split())

C = math.radians(C)
print(0.5*a*b*math.sin(C))
print(a+b+math.sqrt(a*a+b*b-2*a*b*math.cos(C)))
print(b*math.sin(C))