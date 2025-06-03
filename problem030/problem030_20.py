from math import cos, radians, sin, sqrt

def g(a, b, c):
    c_rad = radians(c)
    yield a * b * sin(c_rad) / 2
    yield a + b + sqrt(a ** 2 + b ** 2 - 2 * a * b * cos(c_rad))
    yield b * sin(c_rad)

a, b, c = list(map(int, input().split()))

for i in g(a, b, c):
    print("{:.8f}".format(i))