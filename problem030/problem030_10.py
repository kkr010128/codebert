# coding: utf-8
# Your code here!

import math

a, b, C = map(int, input().split())
S = a * b * 0.5 * math.sin(math.radians(C))
L = a + b + (a * a + b * b - 2 * a * b * math.cos(math.radians(C))) ** 0.5
h = b * math.sin(math.radians(C))

print('{:.8f}'.format(S))
print('{:.8f}'.format(L))
print('{:.8f}'.format(h))
