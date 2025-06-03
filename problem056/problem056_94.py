# -*- coding: utf-8 -*-

import sys
import os


def input_to_list():
    return list(map(int, input().split()))

H, W = input_to_list()
M = []
for i in range(H):
    M.append(input_to_list())

v = []
for i in range(W):
    v.append(int(input()))

# M x v
for i in range(H):
    all = 0
    for j in range(W):
        all += M[i][j] * v[j]
    print(all)