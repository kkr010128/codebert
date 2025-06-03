#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

r, c = map(int, sys.stdin.readline().split())
matrix = list()

for i in range(r):
    _line = list(map(int, sys.stdin.readline().split()))
    _line.append(sum(_line))
    matrix.append(_line)

_line = list()
for col in range(c+1):  # include sum column
    val = 0
    for row in range(r):
        val += matrix[row][col]
    _line.append(val)

matrix.append(_line)
for _line in matrix:
    str_x = list(map(str, _line))
    print(' '.join(str_x))

