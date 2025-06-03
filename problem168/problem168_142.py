#!/usr/bin/env python3
import sys
from itertools import chain


def solve(N: int, M: int, A: "List[int]"):
    answer = N - sum(A)
    if answer < 0:
        answer = -1
    return answer


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    answer = solve(N, M, A)
    print(answer)


if __name__ == "__main__":
    main()
