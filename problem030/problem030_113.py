import math


a, b, C = map(float, input().split())
theta = math.radians(C)
S = 0.5 * a * b * math.sin(theta)
c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(theta))
h = b * math.sin(theta)
print("{:.9f}\n{:.9f}\n{:.9f}".format(S, a+b+c, h))

