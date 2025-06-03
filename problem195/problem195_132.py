import sys
import numpy as np
import heapq


def input():
    return sys.stdin.readline()[:-1]


def solve():
    a = [1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51]
    K = int(input())
    print(a[K-1])


if __name__ == "__main__":
    solve()
