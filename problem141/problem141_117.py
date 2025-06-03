# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
from collections import Counter, defaultdict, deque
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations
from operator import add, mul, sub


import sys
# sys.setrecursionlimit(10**6)
# buff_readline = sys.stdin.buffer.readline
buff_readline = sys.stdin.readline
readline = sys.stdin.readline

INF = 2**62-1


def read_int():
    return int(buff_readline())


def read_int_n():
    return list(map(int, buff_readline().split()))


def read_float():
    return float(buff_readline())


def read_float_n():
    return list(map(float, buff_readline().split()))


def read_str():
    return readline().strip()


def read_str_n():
    return readline().strip().split()

def error_print(*args):
    print(*args, file=sys.stderr)


def mt(f):
    import time

    def wrap(*args, **kwargs):
        s = time.time()
        ret = f(*args, **kwargs)
        e = time.time()

        error_print(e - s, 'sec')
        return ret

    return wrap


@mt
def slv(N, A):
    sa = [0]
    for a in A:
        sa.append(sa[-1]+a)

    if N == 0:
        if A[0] == 1:
            return 1
        else:
            return -1

    if A[0] != 0:
        return -1
        
    ans = 1
    p = 1
    for i in range(1, N+1):
        m = min(p*2, sa[-1] - sa[i])
        ans += m
        if m - A[i] < 0:
            return -1
        p = m - A[i]
    return ans




def main():
    N = read_int()
    A = read_int_n()
    print(slv(N, A))


if __name__ == '__main__':
    main()
