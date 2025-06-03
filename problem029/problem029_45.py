from math import *

x1, y1, x2, y2 = map(float, raw_input().split())
distance = sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))
print distance