#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

n = int(sys.stdin.readline())

for i in range(1, n+1):
    if i % 3 == 0:
        print(' ', i, sep='', end='')
    else:
        x = i
        while x > 0:
            if x % 10 == 3:
                print(' ', i, sep='', end='')
                break
            x //= 10
print()

