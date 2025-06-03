# -*- coding: utf-8 -*-

import sys
import os

a, b = list(map(int, input().split()))

d = a // b
r = a % b
f = a / b

print('{} {} {:.10f}'.format(d, r, f))