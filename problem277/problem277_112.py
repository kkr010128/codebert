import sys

# import re
# import math
# import collections
# import decimal
# import bisect
# import itertools
# import fractions
# import functools
import copy
# import heapq
# import decimal
# import statistics
import queue

sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===


def main():
    h, w, k = ns()
    mat = [list(input()) for _ in range(h)]

    ans_mat = [[0 for i in range(w)] for j in range(h)]

    cnt = 1
    for i in range(h):
        for j in range(w):
            if mat[i][j] == "#":
                ans_mat[i][j] = copy.deepcopy(cnt)
                cnt += 1

    for i in range(h):
        for j in range(1, w):
            if ans_mat[i][j] == 0:
                ans_mat[i][j] = copy.deepcopy(ans_mat[i][j - 1])
        for j in range(w - 2, -1, -1):
            if ans_mat[i][j] == 0:
                ans_mat[i][j] = copy.deepcopy(ans_mat[i][j + 1])

    for i in range(1, h):
        if max(ans_mat[i]) == 0:
            ans_mat[i] = copy.deepcopy(ans_mat[i - 1])
    for i in range(h - 2, -1, -1):
        if max(ans_mat[i]) == 0:
            ans_mat[i] = copy.deepcopy(ans_mat[i + 1])

    for ai in ans_mat:
        print(*ai, sep=" ")


if __name__ == '__main__':
    main()
