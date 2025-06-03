#!/usr/bin/env python3
import sys
from itertools import chain

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(H: int, N: int, A: "List[int]"):
    if H <= sum(A):
        return YES
    else:
        return NO


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    H = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    answer = solve(H, N, A)
    print(answer)


if __name__ == "__main__":
    main()
