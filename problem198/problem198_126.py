import sys
import re
import math
import collections
import decimal
import bisect
import itertools
import fractions
import functools
import copy
import heapq
import decimal
import statistics
import queue

sys.setrecursionlimit(10000001)
INF = 10 ** 10
MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===
def main():
    n = ni()

    char = [chr(i) for i in range(97, 97 + 26)]
    d = [0 for _ in range(11)]
    d[0] = 1

    def printer(d):
        s = ""
        for num in d:
            if num != 0:
                s = char[num - 1] + s

        if len(s) == n:
            print(s)
        return

    while d[n] == 0:
        printer(d)

        d[0] += 1

        for i in range(10):
            if d[i] > max(d[i + 1:]) + 1:
                d[i] = 1
                d[i + 1] += 1


if __name__ == '__main__':
    main()
