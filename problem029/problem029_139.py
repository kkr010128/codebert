# -*- coding: utf-8 -*-

import math

x1, y1, x2, y2 = map(float, raw_input().split())
dx = x2-x1
dy = y2-y1
print math.sqrt(dx*dx+dy*dy)