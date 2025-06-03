import sys
import bisect
import itertools
import collections
import fractions
import heapq
import math
from operator import mul
from functools import reduce
from functools import lru_cache


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    a, b, x = map(int, readline().split())
    if a*a*b/2 < x:
        tan = 2 * b / a - 2 * x / (a ** 3)
        ans = math.degrees(math.atan(tan))
        print(ans)
    else:
        tan = a * b * b / x / 2
        ans = math.degrees(math.atan(tan))
        print(ans)

if __name__ == '__main__':
    solve()