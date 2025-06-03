#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import math

a, b, c = map(float, sys.stdin.readline().split())
degree = abs(180-abs(c))*math.pi / 180

height = abs(b * math.sin(degree))
pos_x = b * math.cos(degree) + a
edge_x = (height**2 + pos_x**2) ** 0.5

print(round(a * height / 2, 6))
print(round(a + b + edge_x, 6))
print(round(height, 6))

