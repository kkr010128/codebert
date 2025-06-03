a, b, h, m = map(int, input().split())
from math import cos,sin, sqrt, radians

x_a = - a * cos(radians(360/12.0*h+360/12/60*m))
y_a = a * sin(radians(360/12.0*h+360/12/60*m))
x_b = - b * cos(radians(360/60.0*m))
y_b = b * sin(radians(360/60.0*m))

print(sqrt((x_a-x_b)**2+(y_a-y_b)**2))