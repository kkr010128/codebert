# -*- coding: utf-8 -*-
# import numpy as np
import sys
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect
import math


def zz():
    return list(map(int, sys.stdin.readline().split()))


def z():
    return int(sys.stdin.readline())


def S():
    return sys.stdin.readline()


def C(line):
    return [sys.stdin.readline() for _ in range(line)]


def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]


N = z()
yakusu_nums = [0]*(N+1)
for i in range(1, N+1):
    for j in range(i, N+1, i):
        yakusu_nums[j] += 1
ans = 0
for i, yakusu_num in enumerate(yakusu_nums):
    # print(i, yakusu_num)
    ans += i*yakusu_num
print(ans)
