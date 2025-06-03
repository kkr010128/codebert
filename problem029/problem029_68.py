import math
x1,y1,x2,y2=(float(x) for x in input().split())
print('{:.05f}'.format(math.sqrt((x2-x1)**2+(y2-y1)**2)))
