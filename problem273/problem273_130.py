import sys
import math
import bisect
import heapq
from collections import Counter


def input():
    return sys.stdin.readline().rstrip()


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    AS = [0]

    it = 0
    for i in range(0, N):
        it += A[i]
        it %= K
        sj = (it - i - 1) % K
        AS.append(sj)
    # 最初だけ作る

    C = dict()
    C[0] = 1
    current = 0
    for j in range(1, N + 1):
        if j > K-1:
            C[AS[j - K]] -= 1
        if AS[j] in C:
            current += C[AS[j]]
            C[AS[j]] += 1
        else:
            C[AS[j]] = 1

    print(current)


if __name__ == "__main__":
    main()
