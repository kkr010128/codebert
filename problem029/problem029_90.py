import math
x1,y1,x2,y2=[float(x) for x in input().split(' ')]
dis=math.sqrt((y2 - y1)**2 + (x2-x1)**2)
print("{:.4f}".format(dis))


