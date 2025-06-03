# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd, ceil, atan, pi
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')
import string
# string.ascii_lowercase
from bisect import bisect_left
MOD = int(1e9)+7
INF = float('inf')


def solve():
    # n, m = [int(x) for x in input().split()]
    n, x, y = [int(x) for x in input().split()]
    
    ans = defaultdict(int)

    for i in range(1, n):
        for j in range(i + 1, n+1):
            d = min(j - i, min(abs(i - x) + 1 + abs(j - y), abs(i - y) + 1 + abs(j - x)))
            ans[d] += 1

    for i in range(1, n):
        print(ans[i])

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

azyxwvutsrqponmlkjihgfedcb

"""
