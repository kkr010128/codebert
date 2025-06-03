# -*- coding: utf-8 -*-
# ITP1_10_A

import math

pos = list(map(float, input().split()))
x = abs(pos[2] - pos[0])
y = abs(pos[3] - pos[1])

print(math.sqrt(x**2 + y**2))

