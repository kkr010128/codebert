import math
a, b, deg = map(float, input().split())
rad = math.radians(deg)
area = 0.5 * a * b * math.sin(rad)
c = math.sqrt(a*a + b*b - 2*a*b*math.cos(rad))
h = area*2 / a;

print(area, a+b+c, h)
