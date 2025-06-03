import math

a, b, ca = map(float, input().split())
ca = math.radians(ca)
s = a * b * math.sin(ca) / 2
c = (a ** 2 + b ** 2 - 2 * a * b * math.cos(ca)) ** 0.5
h = b * math.sin(ca)
print("{:.5f}".format(s))
print("{:.5f}".format(a + b + c))
print("{:.5f}".format(h))
