import math

r = float(input())

if r > 0 and r < 10000:
    circle_length = (r * 2) * math.pi
    circle_area   = r * r * math.pi

    print("{0:f} {1:f}".format(circle_area, circle_length))
else:
    pass