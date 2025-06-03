# import bisect
from collections import Counter, deque
# import copy
# from heapq import heappush, heappop, heapify
# from fractions import gcd
# import itertools
# from operator import attrgetter, itemgetter
# import math

import sys

# import numpy as np

ipti = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    h, w, k = list(map(int,ipti().split()))
    s = [list(input()) for i in range(h)]

    empty_row =  []
    exist_row = []
    berry_id = 1


    for row in range(h):
        is_empty = True
        for col in range(w):
            if s[row][col] == "#":
                s[row][col] = berry_id
                berry_id += 1
                is_empty = False
        if is_empty:
            empty_row.append(row)
        else:
            exist_row.append(row)


    # まず空ではない行を埋める
    for row in range(h):
        if row in exist_row:
            berry_col = deque()
            for col in range(w):
                if s[row][col] != ".":
                    berry_col.append(col)

            first = 0
            fill_id = 0

            while berry_col:
                last = berry_col.popleft()
                fill_id = s[row][last]
                for j in range(first, last+1):
                    s[row][j] =fill_id
                first = last + 1
            for j in range(first, w):
                s[row][j] = fill_id

    for row in empty_row:
        is_filled = False
        for row2 in range(row+1, h):
            if row2 in exist_row:
                for col in range(w):
                    s[row][col] = s[row2][col]
                    is_filled = True
                break
                
        if not is_filled:
            for row2 in range(row-1, -1 , -1):
                if row2 in exist_row:
                    for col in range(w):
                        s[row][col] = s[row2][col]
                        is_filled = True
                    break

    for row in range(h):
        print(*s[row])

if __name__ == '__main__':
    main()