import math
x1, y1, x2, y2 = map(float, input().split())

l = math.sqrt((math.fabs(x1-x2))*(math.fabs(x1-x2))+(math.fabs(y1-y2))*(math.fabs(y1-y2)))

print('%.4f'% l)