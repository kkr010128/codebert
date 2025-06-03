# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
import sys
import resource
from collections import Counter, defaultdict, deque
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations
from operator import add, mul, sub
from copy import deepcopy
sys.setrecursionlimit(1000000)
s, h = resource.getrlimit(resource.RLIMIT_STACK)
# resource.setrlimit(resource.RLIMIT_STACK, (h, h))
input = sys.stdin.readline
INF = 2**62-1


def read_int():
    return int(input())


def read_int_n():
    return list(map(int, input().split()))


def read_float():
    return float(input())


def read_float_n():
    return list(map(float, input().split()))


def read_str():
    return input().strip()


def read_str_n():
    return list(map(str, input().split()))


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
def slv(N, M, S):
    def f(s, p):
        if p == 0:
            return s
        elif p < 0:
            return None
        for i in range(M, 0, -1):
            j = p - i
            if j < 0 or j >= len(S):
                continue
            if S[j] == '1':
                continue
            s.append(i)
            v = f(s, j)
            if v:
                return v
            s.pop()
        return None
    
    m = 0
    mm = 0
    for c in S:
        if c == '1':
            mm += 1
            m = max(mm, m)
        else:
            mm = 0
    if m >= M:
        return -1
            
    ans = f([], N)
    if ans:
        return ' '.join(map(str, reversed(ans)))
    return -1
            

        



def main():
    N, M = read_int_n()
    S = read_str()
    print(slv(N, M, S))


if __name__ == '__main__':
    main()
