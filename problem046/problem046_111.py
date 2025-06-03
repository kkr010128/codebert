# -*- coding: utf-8 -*-

import math

r = float( input() )

area = r * r * math.pi
circle = 2 * r * math.pi

print(format(area, '.10f'), format(circle, '.10f'))