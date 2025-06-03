# -*- coding: utf-8 -*-

import random
import sys
import os
import pprint

#fd = os.open('ALDS1_5_A.txt', os.O_RDONLY)
#os.dup2(fd, sys.stdin.fileno())

n = int(input())
A = list(map(int, input().split()))

# memo table T[i][m]
row_num = len(A)
column_num = 2000
T = [[None for i in range(column_num)] for j in range(row_num)]
#pprint.pprint(T)


def solve(i, m):
    # out of index
    if i >= len(A):
        return False
    if m < 0:
        return False

    if T[i][m] is not None:
        return T[i][m]

    if m == 0:
        T[i][m] = True
    elif m == A[i]:
        T[i][m] = True
    #elif i >= len(A):
    #    T[i][m] = False
    elif solve(i+1, m):
        T[i][m] = True
    elif solve(i+1, m - A[i]):
        T[i][m] = True
    else:
        T[i][m] = False
    return T[i][m]

test_num = int(input())
test_values = map(int, input().split())
for v in test_values:
    result = solve(0, v)
    if result is True:
        print('yes')
    else:
        print('no')