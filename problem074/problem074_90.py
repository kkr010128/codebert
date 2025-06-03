import sys
import os
import math
import bisect
import itertools
import collections
import heapq
import queue
import array

# 時々使う
# from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall
# from decimal import Decimal
# from collections import defaultdict, deque

# 再帰の制限設定
sys.setrecursionlimit(10000000)


def ii(): return int(sys.stdin.buffer.readline().rstrip())
def il(): return list(map(int, sys.stdin.buffer.readline().split()))
def fl(): return list(map(float, sys.stdin.buffer.readline().split()))
def iln(n): return [int(sys.stdin.buffer.readline().rstrip())
                    for _ in range(n)]


def iss(): return sys.stdin.buffer.readline().decode().rstrip()
def sl(): return list(map(str, sys.stdin.buffer.readline().decode().split()))
def isn(n): return [sys.stdin.buffer.readline().decode().rstrip()
                    for _ in range(n)]


def lcm(x, y): return (x * y) // math.gcd(x, y)


# MOD = 10 ** 9 + 7
MOD = 998244353
INF = float('inf')


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    N, K = il()
    D = [il() for _ in range(K)]

    dp = [0] * (N)
    dp[0] = 1
    acc = 0
    for i in range(1, N):
        for l, r in D:
            if i - l >= 0:
                acc += dp[i-l]
                acc %= MOD
            if i - r - 1 >= 0:
                acc -= dp[i-r-1]
                acc %= MOD
        dp[i] = acc
    print(dp[-1])


if __name__ == '__main__':
    main()
