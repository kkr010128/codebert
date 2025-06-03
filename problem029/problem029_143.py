import math

data = input().split()
x1 = float(data[0])
x2 = float(data[2])
y1 = float(data[1])
y2 = float(data[3])
x3 = x1 - x2 if x1 > x2 else x2 - x1
y3 = y1 - y2 if y1 > y2 else y2 - y1
print("%.8f" % math.sqrt(x3 * x3 + y3 * y3))
