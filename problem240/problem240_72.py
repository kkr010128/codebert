# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    n, m = [int(x) for x in input().split()]
    ac = set()
    pen = defaultdict(int)
    pp = 0
    for _ in range(m):
        p, S = [x for x in input().split()]
        if p not in ac and S == 'AC':
            ac.add(p)
            pp += pen[p]
        else:
            if not p in ac:
                pen[p] += 1

    print(len(ac), pp)

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""


"""
