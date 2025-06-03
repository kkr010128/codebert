
import math

z = raw_input()
x1, y1, x2, y2 = z.split()
x1 = float(x1)
x2 = float(x2)
y1 = float(y1)
y2 = float(y2)

d = math.sqrt((x2 - x1) * (x2-x1) + (y2 - y1) * (y2 - y1))

print ("%lf" %(d))