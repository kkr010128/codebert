# -*- coding: utf-8 -*-
# input
a, b = map(int, input().split())
x = list(map(int, input().split()))
x.sort()
o = 0
for i in range(b):
    o = o+x[i]
print(o)
