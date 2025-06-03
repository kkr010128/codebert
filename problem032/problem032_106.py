# -*- coding: utf-8 -*-

import math

n = int(raw_input())
x = map(int, raw_input().split())
y = map(int, raw_input().split())
d1 = d2 = d3 = d4 = 0.0
for i in range(n):
    d = math.fabs(x[i]-y[i])
    d1 += d
    d2 += d*d
    d3 += d*d*d
    if d4 < d:
        d4 = d
d2 = math.pow(d2, (1.0/2.0))
d3 = math.pow(d3, (1.0/3.0))

print d1
print d2
print d3
print d4