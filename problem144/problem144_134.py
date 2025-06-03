import math

a, b, h, m = map(int, input().split())

min = h * 60 + m
short = 0.5 * min
long = 6 * m

if abs(short - long) >= 180:
    deg = 360 - abs(short - long)

else:
    deg = abs(short - long)

coss = math.cos(math.radians(deg))
c = (a ** 2 + b ** 2 - 2 * a * b * coss) ** 0.5
#print(c)
print('{:.20f}'.format(c))
