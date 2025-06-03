#!/usr/bin/env python3
import sys
from itertools import chain


def solve(N: int, A: "List[int]"):
    s = [0 for _ in range(N)]
    for Ai in A:
        s[Ai - 1] += 1

    return "\n".join(map(str, s))


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    N = int(next(tokens))  # type: int
    A = [
        int(next(tokens)) for _ in range(N - 2 + 1)
    ]  # type: "List[int]"
    answer = solve(N, A)
    print(answer)


if __name__ == "__main__":
    main()
