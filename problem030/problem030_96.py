# -*- coding: utf-8 -*-

import math

a, b, C = map(int, raw_input().split())
radC = math.radians(C)
c = math.sqrt(a*a+b*b-2*a*b*math.cos(radC))
S = a*b/2*math.sin(radC)
print S
print a+b+c
print 2*S/a