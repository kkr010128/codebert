#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

x1, y1, x2, y2 = map(float, sys.stdin.readline().split())
print(round(((x2-x1)**2 + (y2-y1)**2) ** 0.5, 6))

