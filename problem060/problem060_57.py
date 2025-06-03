#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

n, m, p = map(int, sys.stdin.readline().split())
mat_a = list()
mat_b = list()

for i in range(n):
    mat_a.append(list(map(int, sys.stdin.readline().split())))

for i in range(m):
    mat_b.append(list(map(int, sys.stdin.readline().split())))

mat_c = [[0 for i in range(p)] for k in range(n)]

for row in range(n):
    for col in range(p):
        for k in range(m):
            mat_c[row][col] += mat_a[row][k]*mat_b[k][col]
    str_x = list(map(str, mat_c[row]))
    print(' '.join(str_x))

