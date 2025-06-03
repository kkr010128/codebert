# -*- coding: utf-8 -*-

r, c = map(int, raw_input().split())
mat = {}
for i in range(1, r+1):
    col = map(int, raw_input().split())
    for j in range(1, c+1):
        mat[(i, j)] = col[j-1]

for i in range(1, r+1):
    mat[(i, c+1)] = 0
    for j in range(1, c+1):
        mat[(i, c+1)] += mat[(i, j)]

for j in range(1, c+2):
    mat[(r+1, j)] = 0
    for i in range(1, r+1):
        mat[(r+1, j)] += mat[(i, j)]

for i in range(1, r+2):
    buf = ""
    for j in range(1, c+1):
        buf += str(mat[(i, j)]) +" "
    buf += str(mat[(i, c+1)])
    print buf