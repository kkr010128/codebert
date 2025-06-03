#!/usr/bin/env python3
import sys
from itertools import chain

# form bisect import bisect_left, bisect_right, insort_left, insort_right
# from collections import Counter
# import numpy as np


def solve(N: int, K: int, p: "List[int]"):
    p = sorted(p)
    return sum(p[:K])


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    # N, K, p = map(int, line.split())
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    p = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    answer = solve(N, K, p)
    print(answer)


if __name__ == "__main__":
    main()
