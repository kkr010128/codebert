#!/usr/bin/env python3
import sys
from itertools import chain

# form bisect import bisect_left, bisect_right, insort_left, insort_right
# import numpy as np

# 7.n = 7 * 1.n = 101
7777


def solve(K: int):
    n = 7
    for answer in range(1, K + 1):
        if n % K == 0:
            return answer
        n = 10 * (n % K) + 7
    return -1


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    # K = map(int, line.split())
    K = int(next(tokens))  # type: int
    answer = solve(K)
    print(answer)


if __name__ == "__main__":
    main()
