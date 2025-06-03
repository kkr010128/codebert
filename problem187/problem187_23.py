import sys
import os
import math
import bisect
import collections
import itertools
import heapq
import re
import queue
from decimal import Decimal

# import fractions

sys.setrecursionlimit(10000000)

ii = lambda: int(sys.stdin.buffer.readline().rstrip())
il = lambda: list(map(int, sys.stdin.buffer.readline().split()))
fl = lambda: list(map(float, sys.stdin.buffer.readline().split()))
iln = lambda n: [int(sys.stdin.buffer.readline().rstrip()) for _ in range(n)]

iss = lambda: sys.stdin.buffer.readline().decode().rstrip()
sl = lambda: list(map(str, sys.stdin.buffer.readline().decode().split()))
isn = lambda n: [sys.stdin.buffer.readline().decode().rstrip() for _ in range(n)]

lcm = lambda x, y: (x * y) // math.gcd(x, y)
# lcm = lambda x, y: (x * y) // fractions.gcd(x, y)

MOD = 10 ** 9 + 7
MAX = float('inf')


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    N, X, Y = il()

    k = {n:0 for n in range(N-1)}
    X -= 1
    Y -= 1
    for i in range(N-1):
        for j in range(i+1, N):
            m = min(abs(i-j), abs(X-i) + abs(Y-j) + 1, abs(X-j) + abs(Y-i) + 1)
            k[m-1] += 1

    for i in range(len(k)):
        print(k[i])


if __name__ == '__main__':
    main()
