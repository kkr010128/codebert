#!/usr/bin/env python3
import math
n, a, b = map(int, input().split())

c = a + b
d = n % c
e = n // c

if d <= a:
    print(e * a + d)
else:
    print((e + 1) * a)
