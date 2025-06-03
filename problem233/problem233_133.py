#!/usr/bin/env python3
import sys
from itertools import chain

# import numpy as np
# from itertools import combinations as comb
# from bisect import bisect_left, bisect_right, insort_left, insort_right
# from collections import Counter


def solve(N: int, P: "List[int]"):
    min_p = P[0]
    count = 0
    for p in P:
        if p <= min_p:
            min_p = p
            count += 1

    return count


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    N = int(next(tokens))  # type: int
    P = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    answer = solve(N, P)
    print(answer)


if __name__ == "__main__":
    main()
