from math import sqrt
x1, y1, x2, y2 = map(float, input().split())
r = sqrt((x1 - x2)**2 + (y1 - y2)**2 )
print('{0:.5f}'.format(r))
