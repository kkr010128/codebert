#!/usr/bin/env python3
import math

a, b, x = [int(s) for s in input().split()]

b_w = x / (a * a)

x1 = 2 * b_w - b

if x1 >= 0:
    print(math.atan((b - x1) / a) / (2*math.pi) * 360)
else:
    print(math.atan(b * a * b / x / 2) / (2*math.pi) * 360)
