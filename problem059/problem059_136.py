# -*- coding: utf-8 -*-

r, c = list(map(int, input().split()))
a = []
line_sum = 0

for i in range(r):
    a.append(list(map(int, input().split())))

for i in range(r):
    for j in range(c + 1):
        if j == c:
            print('{0}'.format(sum(a[i])))
            line_sum += sum(a[i])
        else:
            print('{0} '.format(a[i][j]), end='')

for i in range(c):
    column_sum = 0
    for j in range(r):
        column_sum += a[j][i]

    print('{0} '.format(column_sum), end='')

print(line_sum)
