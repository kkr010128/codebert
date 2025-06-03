#!/usr/bin/env python3
import sys
from itertools import chain

# form bisect import bisect_left, bisect_right, insort_left, insort_right
# from collections import Counter
# import numpy as np


def solve(N: int):
    az = "abcdefghijklmnopqrstuvwxyz"
    N -= 1
    answer = ""
    while True:
        answer = az[N % 26] + answer
        N = N // 26
        if N == 0:
            break
        N = N - 1
    return answer


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    # N = map(int, line.split())
    N = int(next(tokens))  # type: int
    answer = solve(N)
    print(answer)


if __name__ == "__main__":
    main()
