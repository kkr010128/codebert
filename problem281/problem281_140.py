# coding=utf-8
from math import floor, ceil, sqrt, factorial, log, gcd
from itertools import accumulate, permutations, combinations, product, combinations_with_replacement
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush, heappushpop
import copy
import numpy as np
import sys
INF = float('inf')
mod = 10**9+7
sys.setrecursionlimit(10 ** 6)


def lcm(a, b): return a * b / gcd(a, b)

# 1 2 3
# a, b, c = LI()


def LI(): return list(map(int, sys.stdin.buffer.readline().split()))

# a = I()


def I(): return int(sys.stdin.buffer.readline())

# abc def
# a, b = LS()


def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()

# a = S()


def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')

# 2
# 1
# 2
# [1, 2]


def IR(n): return [I() for i in range(n)]

# 2
# 1 2 3
# 4 5 6
# [[1,2,3], [4,5,6]]


def LIR(n): return [LI() for i in range(n)]

# 2
# abc
# def
# [abc, def]


def SR(n): return [S() for i in range(n)]

# 2
# abc def
# ghi jkl
# [[abc,def], [ghi,jkl]]


def LSR(n): return [LS() for i in range(n)]

# 2
# abcd
# efgh
# [[a,b,c,d], [e,f,g,h]]


def SRL(n): return [list(S()) for i in range(n)]


def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p


fact = [1, 1]  # n! mod p
factinv = [1, 1]  # (n!)^(-1) mod p
tmp = [0, 1]  # factinv 計算用


def main():
    x, y = LI()
    ans = 0
    if x > 2 * y or x < 0.5 * y or (x + y) % 3 != 0:
        print(0)
        return
    n, m = map(int, [(2 * y - x) / 3, (2 * x - y) / 3])

    for i in range(2, n + m + 1):
        fact.append((fact[-1] * i) % mod)
        tmp.append((-tmp[mod % i] * (mod // i)) % mod)
        factinv.append((factinv[-1] * tmp[-1]) % mod)

    print(cmb(n+m, n, mod))


if __name__ == "__main__":
    main()
