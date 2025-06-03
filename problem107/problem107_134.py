import sys
from collections import deque
import bisect
import copy
import heapq
import itertools
import math
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
mod = 10 ** 9 + 7

def read_values(): return map(int, input().split())
def read_index(): return map(lambda x: int(x) - 1, input().split())
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]


def f(N):
    res = 0
    while N != 0:
        b = format(N, "b").count("1")
        N %= b
        res += 1
    return res


def main():
    N = int(input())
    X = input().strip()
    K = X.count("1")

    A = [(1, 1)]
    for i in range(N):
        a, b = A[-1]
        A.append(((a * 2) % (K - 1) if K != 1 else 0, (b * 2) % (K + 1)))

    B = [0, 0]
    for i, b in enumerate(X[::-1]):
        if b == "0":
            continue
        if K != 1:
            B[0] += A[i][0]
            B[0] %= K - 1
        B[1] += A[i][1]
        B[1] %= K + 1

    res = [0] * N
    for i, b in enumerate(X[::-1]):
        if b == "0":
            res[i] = (B[1] + A[i][1]) % (K + 1)
        else:
            if K == 1:
                res[i] = 0
                continue
            res[i] = (B[0] - A[i][0]) % (K - 1)
        res[i] = f(res[i]) + 1

    for r in res[::-1]:
        print(r)


if __name__ == "__main__":
    main()
