from math import cos, radians, sqrt

a, b, h, m = map(int, input().split())
angle = radians(h*30 + m / 2- m*6)
print(sqrt(a**2 + b**2 - 2*a*b*cos(angle)))