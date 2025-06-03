# -*- coding: utf-8 -*-

mat1 = {}
mat2 = {}

n, m, l = map(int, raw_input().split())
for i in range(1, n+1):
    list = map(int, raw_input().split())
    for j in range(1, m+1):
        mat1[(i, j)] = list[j-1]

for j in range(1, m+1):
    list = map(int, raw_input().split())
    for k in range(1, l+1):
        mat2[(j, k)] = list[k-1]

for i in range(1, n+1):
    buf = ""
    for k in range(1, l+1):
        res = 0
        for j in range(1, m+1):
            res += mat1[(i, j)]*mat2[(j, k)]
        buf += str(res) +" "
    buf = buf.rstrip()
    print buf