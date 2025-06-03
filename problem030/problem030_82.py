# -*- coding: utf-8 -*-

import math

a, b, C = map(float, input().split())
c = math.sqrt((a * a) + (b * b) - 2 * a * b * math.cos(math.radians(C)))
s = (a * b * math.sin(math.radians(C))) / 2
l = a + b + c
h = (2 * s) / a
print(s)
print(l)
print(h)
