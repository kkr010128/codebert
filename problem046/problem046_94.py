import math
r = float(input())
areaOfCircle = format(r * r * math.pi, '.6f')
circumference = format(2 * r * math.pi,'.6f')
print("{0} {1}".format(areaOfCircle, circumference))