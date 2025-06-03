#!/usr/bin/env python3
import sys
from itertools import chain

# from itertools import combinations as comb
# form bisect import bisect_left, bisect_right, insort_left, insort_right
# from collections import Counter
# import numpy as np

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(X: int, Y: int):
    if Y % 2 == 1:
        return NO
    if Y > X * 4:
        return NO
    if Y < X * 2:
        return NO
    return YES


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    answer = solve(X, Y)
    print(answer)


if __name__ == "__main__":
    main()
