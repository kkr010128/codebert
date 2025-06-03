
from math import cos, pi

A, B, H, M = map(int, input().split())

theta = abs(M * 6 - (H * 30 + M / 2)) / 360 * 2 * pi
c = (A ** 2 + B ** 2 - 2 * A * B * cos(theta)) ** 0.5
print(c)
