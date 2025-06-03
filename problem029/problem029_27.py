a, b, c, d = [float(temp) for temp in input().split()]
from math import sqrt
dis = sqrt((c - a) ** 2 + (d - b) ** 2)
print('%0.5f'%dis)