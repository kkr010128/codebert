import math
a, b, h, m = [int(i) for i in input().split()]
theta = math.radians(h / 12 * 360 - m / 60 * 360 + m / 60 / 12 * 360)
print(math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(theta)))