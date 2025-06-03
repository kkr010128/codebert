import math
a, b, c = map(int, raw_input().split())
radius = c / 180.0 * math.pi
h = b * math.sin(radius)
print (a * h) / 2.0
print a + b + math.sqrt(a**2 + b**2 - 2*a*b*math.cos(radius))
print h