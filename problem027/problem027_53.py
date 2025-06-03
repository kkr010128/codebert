# -*- coding: utf-8 -*-

import sys
import os
import math


n = int(input())
p0 = (0, 0)
p1 = (100, 0)

def koch(depth, p0, p1):
    if depth == 0:
        return

    # s = 2/3 p0 + 1/3 p1
    sx = 2 / 3 * p0[0] + 1 / 3 * p1[0]
    sy = 2 / 3 * p0[1] + 1 / 3 * p1[1]
    s = (sx, sy)

    tx = 1 / 3 * p0[0] + 2 / 3 * p1[0]
    ty = 1 / 3 * p0[1] + 2 / 3 * p1[1]
    t = (tx, ty)

    theta = math.radians(60)
    ux = math.cos(theta) * (tx - sx) - math.sin(theta) * (ty - sy) + sx
    uy = math.sin(theta) * (tx - sx) + math.cos(theta) * (ty - sy) + sy
    u = (ux, uy)

    # ????????? s, u, t?????¨???
    koch(depth - 1, p0, s)
    print(*s)
    koch(depth - 1, s, u)
    print(*u)
    koch(depth - 1, u, t)
    print(*t)
    koch(depth - 1, t, p1)

print(*p0)
koch(n, p0, p1)
print(*p1)