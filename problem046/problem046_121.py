import math

i = float(input())
area = float(math.pi * i * i)
length = float(2 * math.pi * i)

print('{0:.6f} {1:.6f}'.format(area, length))