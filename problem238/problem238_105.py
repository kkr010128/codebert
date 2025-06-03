# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    n, k, s = [int(x) for x in input().split()]
    ans = [0] * n
    for i in range(n):
        if i < k:
            ans[i] = s
        else:
            x = n - k
            z = s + 1
            if s == int(1e9):
                z -= 10
            ans[i] = z
    print(*ans)


t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

abc

"""
