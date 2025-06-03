# -*- coding: utf-8 -*-

n, m, l = list(map(int, input().split()))
a = []
b = []

for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(m):
    b.append(list(map(int, input().split())))

for i in range(n):
    for j in range(l):
        mat_sum = 0
        for k in range(m):
            mat_sum += a[i][k] * b[k][j]
        if j == l - 1:
            print('{0}'.format(mat_sum), end='')
        else:
            print('{0} '.format(mat_sum), end='')
    print()
