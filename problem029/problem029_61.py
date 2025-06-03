# -*- coding: utf-8 -*-

import sys
import os
import math


x1, y1, x2, y2 = list(map(float, input().split()))
x_diff = x1 - x2
y_diff = y1 - y2
d = math.sqrt(x_diff ** 2 + y_diff ** 2)
print(d)