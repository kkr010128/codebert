#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

n = int(sys.stdin.readline())
debt = 100000
for i in range(n):
    debt += debt // 20
    fraction = debt % 1000
    if fraction > 0:
        debt += 1000 - fraction
print(debt)