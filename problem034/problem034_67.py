#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

face = sys.stdin.readline().split()

right = [[None for front in range(6)] for top in range(6)]

# Top:1 Face:2 -> Right:3, Top:2 Face:6 -> Right:3 ...
right[0][1] = right[1][5] = right[5][4] = right[4][0] = 3 - 1
right[1][0] = right[5][1] = right[4][5] = right[0][4] = 4 - 1
right[0][2] = right[2][5] = right[5][3] = right[3][0] = 5 - 1
right[2][0] = right[5][2] = right[3][5] = right[0][3] = 2 - 1
right[3][1] = right[1][2] = right[2][4] = right[4][3] = 1 - 1
right[1][3] = right[2][1] = right[4][2] = right[3][4] = 6 - 1

# print(right)

q = int(sys.stdin.readline())
for i in range(q):
    top, front = sys.stdin.readline().split()
    r_index = right[face.index(top)][face.index(front)]
    print(face[r_index])

