from math import sin, cos, radians
a, b, ang = map(int, input().split())
ang = radians(ang)
area = a * b * sin(ang) / 2
c = (a ** 2 + b ** 2 - 2 * a * b * cos(ang)) ** 0.5
circ = a + b + c
height = area * 2 / a
print("%lf\n%lf\n%lf" % (area, circ, height))
