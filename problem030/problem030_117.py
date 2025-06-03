import math

data = map(int, raw_input().split())
a = data[0]
b = data[1]
deg = math.radians(data[2])

c = (a**2 + b**2 - 2*a*b*math.cos(deg))**0.5
L = a + b + c
h = b * math.sin(deg)
S = a * h * 0.5

print S
print L
print h