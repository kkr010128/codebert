#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
n = input()
debt = 1e5
for i in range(0, n):
    debt *= 1.05
    debt = math.ceil(debt/1000) * 1000
print int(debt)