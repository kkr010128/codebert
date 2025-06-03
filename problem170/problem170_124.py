import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def inp():
    return int(input())
def inps():
    return input().rstrip()
def inpl():
    return list(map(int, input().split()))
def _debug(obj):
    print(obj, file=sys.stderr)

# import decimal
# from decimal import Decimal
# decimal.getcontext().prec = 10

# from heapq import heappush, heappop, heapify
# import math
# from math import gcd
# import itertools as it
# import collections
# from collections import deque 

# ---------------------------------------

mod = 10**9 +7
N, K = inpl()

ans = 0
for i in range(K, N + 2):
    ans += (N + 1 - i) * i + 1
    ans %= mod

print(ans)