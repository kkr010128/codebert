from collections import Counter, defaultdict
import sys
sys.setrecursionlimit(10 ** 5 + 10)
# input = sys.stdin.readline
from math import factorial
import heapq, bisect
import math
import itertools
import queue
from collections import deque
from fractions import Fraction

def comb(n, r, mod):
    ans = 1
    for i in range(max(r, n - r) + 1, n + 1):
        ans *= i
        ans %= mod
    for i in range(1, min(r, n - r) + 1):
        ans *= pow(i, mod - 2, mod)
        ans %= mod
    return ans


def main():
    x, y = map(int, input().split())

    if (x + y) % 3 != 0:
        print(0)
        sys.exit()

    tate = (2 * y - x) // 3
    yoko = (2 * x - y) // 3

    if tate < 0 or yoko < 0:
        print(0)
        sys.exit()

    mod = 10 ** 9 + 7
    ans = comb(tate + yoko, tate, mod)
    print(ans)







if __name__ == '__main__':
    main()

