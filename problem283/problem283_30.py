#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pdb
import sys
F = sys.stdin
N = int(F.readline())
count = 0

A = N // 2

for i in range(1, A+1):
    if i*2 != N:
        count += 1

print(count)
