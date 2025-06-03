#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

while True:
    s = sys.stdin.readline().strip()
    if s == '0':
        break
    total = 0
    for c in s:
        total += int(c)
    print(total)

