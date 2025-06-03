# -*- coding: utf-8 -*-

import sys
import os


def input_to_list():
    return list(map(int, input().split()))

H, W = input_to_list()
M = []
for i in range(H):
    lis = input_to_list()
    s = sum(lis)
    lis.append(s)
    M.append(lis)

# vertical sum
last = []
for i in range(W + 1):
    s = 0
    for j in range(H):
        s += M[j][i]
    last.append(s)
M.append(last)

# print
for i in range(H + 1):
    print(*M[i])