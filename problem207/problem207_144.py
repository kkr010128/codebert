"""Boot-camp-for-Beginners_Easy007_B_Bingo_25-August-2020.py"""
import numpy as np
import sys

A = list(list(map(int, input().split())) for i in range(3))
N = int(input())
b = list(int(input()) for i in range(N))

MARK = []
for k in range(N):
    for i in range(3):
        for j in range(3):
            if(A[i][j] == b[k]):
                MARK.append([i-1, j-1])
# print(MARK)
count_row_m1, count_row_0, count_row_p1, count_column_m1, count_column_0, count_column_p1, count_backslash, count_slash = 0, 0, 0, 0, 0, 0, 0, 0
for k in range(len(MARK)):
    if MARK[k][0] == -1:
        count_column_m1 += 1
    elif MARK[k][0] == 0:
        count_column_0 += 1
    else:
        count_column_p1 += 1

    if MARK[k][1] == -1:
        count_row_m1 += 1
    elif MARK[k][1] == 0:
        count_row_0 += 1
    else:
        count_row_p1 += 1

    if MARK[k][0] == MARK[k][1]:
        count_backslash += 1
    if MARK[k][0] == -MARK[k][1]:
        count_slash += 1
bingo = count_row_m1 >= 3 or count_row_0 >= 3 or count_row_p1 >= 3 or count_column_m1 >= 3 or count_column_0 >= 3 or count_column_p1 >= 3 or count_backslash >= 3 or count_slash >= 3
"""
print("count_column_m1", count_column_m1)
print("count_column_0", count_column_0)
print("count_column_p1", count_column_p1)
print("count_row_m1", count_row_m1)
print("count_row_0", count_row_0)
print("count_row_p1", count_row_p1)
print("count_backslash", count_backslash)
print("count_slash", count_slash)
"""
if bingo == True:
    print("Yes")
else:
    print("No")
