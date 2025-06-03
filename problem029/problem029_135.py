import math

x1,y1,x2,y2 = tuple(float(n) for n in input().split())
D = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print("{:.8f}".format(D))
