import math
a, b, h, m = map(int, input().split())

dega = - 30*h - 0.5*m + 90
degb = - 6*m + 90

x_a = a*math.cos(math.radians(dega))
y_a = a*math.sin(math.radians(dega))
x_b = b*math.cos(math.radians(degb))
y_b = b*math.sin(math.radians(degb))
# print(dega, degb)
# print(x_a, x_b, y_a, y_b)
print(((x_a-x_b)**2+(y_a-y_b)**2)**0.5)
