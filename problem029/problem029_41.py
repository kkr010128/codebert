x1, y1, x2, y2 = map(float, input().split())

X = (x2 - x1)**2
Y = (y2 - y1)**2

distance = (X + Y)**(1/2)
print("%.8f" % (float(distance)))