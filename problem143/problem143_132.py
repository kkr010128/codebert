#!/usr/bin/env python3
import sys
from itertools import chain


def solve(K: int, S: str):
    if len(S) <= K:
        return S
    else:
        return S[:K] + "..."


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    K = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    answer = solve(K, S)
    print(answer)


if __name__ == "__main__":
    main()
