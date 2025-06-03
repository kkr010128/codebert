import math

r = input()
r = float(r)

area = math.pi * (r ** 2)
length = 2 * math.pi * r

print("{0:.5f} {1:.5f}".format(area, length))