#!/usr/bin/env python3
from itertools import combinations
import sys
input = sys.stdin.readline
MOD = 10**9 + 7

t1, t2 = [int(item) for item in input().split()]
a1, a2 = [int(item) for item in input().split()]
b1, b2 = [int(item) for item in input().split()]
a1 *= t1
b1 *= t1
a2 *= t2
b2 *= t2

if a1 + a2 == b1 + b2:
    print("infinity")
    exit()
if a1 + a2 > b1 + b2:
    a1, a2, b1, b2 = b1, b2, a1, a2

diff = (b1 + b2) - (a1 + a2)
mid_diff = b1 - a1
if mid_diff > 0:
    print(0)
else:
    ans = (abs(mid_diff) + diff - 1) // diff * 2
    if abs(mid_diff) % diff == 0:
        ans += 1
    print(ans - 1)