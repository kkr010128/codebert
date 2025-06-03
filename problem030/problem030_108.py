import math

a, b, C = map(float, input().split())

h = b * math.sin(math.radians(C))
S = a * h / 2

a1 = b * math.cos(math.radians(C))
cc = math.sqrt(h * h + (a - a1) * (a - a1))

print("{a:5f}".format(a=S))
print("{a:5f}".format(a=a + b + cc))
print("{a:5f}".format(a=h))

