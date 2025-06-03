import math

a, b, h, m = map(int, input().split())

minute = 60 * h + m
argA = minute / 720 * 2 * math.pi
argB = minute / 60 * 2 * math.pi
a_x = a * math.cos(argA)
a_y = a * math.sin(argA)
b_x = b * math.cos(argB)
b_y = b * math.sin(argB)
d = math.sqrt((a_x - b_x) ** 2 + (a_y - b_y) ** 2)

print(d)