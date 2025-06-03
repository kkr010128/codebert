#!/usr/bin/env python3
import sys
from itertools import chain
from collections import Counter

# form bisect import bisect_left, bisect_right, insort_left, insort_right
# import numpy as np


def solve(N: int, S: "List[str]"):
    d = Counter(S)
    for key in ("AC", "WA", "TLE", "RE"):
        print(f"{key} x {d.get(key, 0)}")


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    # N, S = map(int, line.split())
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, S)


if __name__ == "__main__":
    main()
