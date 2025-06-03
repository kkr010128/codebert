#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

a, b, c = map(int, sys.stdin.readline().split())

num_div = 0

for x in range(a, b+1):
    if c % x == 0:
        num_div += 1

print(num_div)

