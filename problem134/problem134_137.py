#!/usr/bin/env python3
import sys
from itertools import chain

MAX = 10 ** 18


def solve(N: int, A: "List[int]"):
    A = sorted(A)
    answer = 1
    for a in A:
        answer *= a
        if answer > MAX:
            return -1
    return answer


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    # N, A = map(int, line.split())
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    answer = solve(N, A)
    print(answer)


if __name__ == "__main__":
    main()
