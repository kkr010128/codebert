import math

x1, y1, x2, y2 = [float(i) for i in input().split()]

bottom = x2 - x1
height = y2 - y1

print(math.sqrt(bottom**2 + height**2))