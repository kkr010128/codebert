# -*- coding: utf-8 -*-

import sys

rectangle = []
h,w = 1,1

while not(h == 0 and w == 0):
    h,w = map(int, input().split())
    if not(h == 0 and w == 0):
        rectangle.append([h,w])

for rec in rectangle:
    row_count = 1
    display = []
    for row in range(rec[0]):
        col_count = 0
        if (row_count %2 == 1):
            col_count = 1
        else:
            col_count = 2
        for col in range(rec[1]):
            if (col_count % 2 == 1):
                display.append('#')
            else:
                display.append('.')
            col_count += 1
        row_count += 1
        display.append('\n')
    print(''.join(display))