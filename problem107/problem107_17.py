# -*- coding: utf-8 -*-
import sys
import math
import os
import itertools
import string
import heapq
import _collections
from collections import Counter
from collections import defaultdict
from collections import deque
from functools import lru_cache
import bisect
import re
import queue
import copy
import decimal


class Scanner():
    @staticmethod
    def int():
        return int(sys.stdin.readline().rstrip())

    @staticmethod
    def string():
        return sys.stdin.readline().rstrip()

    @staticmethod
    def map_int():
        return [int(x) for x in Scanner.string().split()]

    @staticmethod
    def string_list(n):
        return [Scanner.string() for i in range(n)]

    @staticmethod
    def int_list_list(n):
        return [Scanner.map_int() for i in range(n)]

    @staticmethod
    def int_cols_list(n):
        return [Scanner.int() for i in range(n)]


def pop_count(x):
    x = x - ((x >> 1) & 0x5555555555555555)
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
    x = x + (x >> 8)
    x = x + (x >> 16)
    x = x + (x >> 32)
    return x & 0x0000007f


def f(x):
    if x == 0:
        return 0
    return f(x % pop_count(x)) + 1


def solve():
    N = Scanner.int()
    S = Scanner.string()
    pc = sum([s == '1' for s in S])
    ans = [0 for _ in range(N)]
    for b in range(2):
        npc = pc
        if b == 0:
            npc += 1
        else:
            npc -= 1
        if npc <= 0:
            continue
        r0 = 0
        for i in range(N):
            r0 = ((r0 * 2) + int(S[i])) % npc
        k = 1
        for i in reversed(range(N)):
            if int(S[i]) == b:
                r = r0
                if b == 0:
                    r = (r + k) % npc
                else:
                    r = (r - k + npc) % npc
                ans[i] = f(r) + 1
            k = (k * 2) % npc
    print(*ans, sep='\n')


def main():
    sys.setrecursionlimit(1000000)
    # sys.stdin = open("sample.txt")
    # T = Scanner.int()
    # for _ in range(T):
    #     solve()
    # print('YNeos'[not solve()::2])
    solve()


if __name__ == "__main__":
    main()
