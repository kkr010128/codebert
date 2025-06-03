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
from functools import lru_cache
import bisect
import re
import queue
from decimal import *


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
        return [input() for i in range(n)]

    @staticmethod
    def int_list_list(n):
        return [Scanner.map_int() for i in range(n)]

    @staticmethod
    def int_cols_list(n):
        return [int(input()) for i in range(n)]


class Math():
    @staticmethod
    def gcd(a, b):
        if b == 0:
            return a
        return Math.gcd(b, a % b)

    @staticmethod
    def lcm(a, b):
        return (a * b) // Math.gcd(a, b)

    @staticmethod
    def divisor(n):
        res = []
        i = 1
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                res.append(i)
                if i != n // i:
                    res.append(n // i)
        return res

    @staticmethod
    def round_up(a, b):
        return -(-a // b)

    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        d = int(n ** 0.5) + 1
        for i in range(3, d + 1, 2):
            if n % i == 0:
                return False
        return True


def pop_count(x):
    x = x - ((x >> 1) & 0x5555555555555555)
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
    x = x + (x >> 8)
    x = x + (x >> 16)
    x = x + (x >> 32)
    return x & 0x0000007f


MOD = int(1e09) + 7
INF = int(1e15)


def solve():
    H, W, K = Scanner.map_int()
    S = Scanner.string_list(H)

    ans = [[0 for _ in range(W)] for _ in range(H)]

    vec = []
    for h in range(H):
        if S[h].count('#') > 0:
            vec.append(h)

    for i in range(len(vec)):
        v1, v2 = 0, H - 1
        if i > 0:
            v1 = vec[i - 1] + 1
        if i < len(vec) - 1:
            v2 = vec[i]

        vec2 = []
        for w in range(W):
            cnt = 0
            for h in range(v1, v2 + 1):
                if S[h][w] == '#':
                    cnt += 1
            if cnt > 0:
                vec2.append(w)
        for j in range(len(vec2)):
            w1, w2 = 0, W - 1
            if j > 0:
                w1 = vec2[j - 1] + 1
            if j < len(vec2) - 1:
                w2 = vec2[j]
            for h in range(v1, v2 + 1):
                for w in range(w1, w2 + 1):
                    ans[h][w] = K
            K -= 1
    for a in ans:
        print(*a)


def main():
    # sys.stdin = open("sample.txt")
    solve()


if __name__ == "__main__":
    main()
