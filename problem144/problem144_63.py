import math

a, b, h, m = map(int, input().split())

omg_s = math.pi / 360
omg_l = math.pi / 30

tht = (60*h + m)*omg_s - m*omg_l

c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(tht))
print(c)