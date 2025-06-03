# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd, ceil
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')
import string
# string.ascii_lowercase
from bisect import bisect_left

def solve():
    n = int(input())
    l = [int(x) for x in input().split()]
    l.sort()
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            r = bisect_left(l, l[i] + l[j])
            # if r > j:
            ans += r - j - 1
    print(ans)

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

azyxwvutsrqponmlkjihgfedcb

"""
