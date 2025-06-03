#!/usr/bin/env python3
import sys
from itertools import chain
from bisect import bisect_right

# from collections import Counter
# import numpy as np


def solve(N: int, M: int, K: int, A: "List[int]", B: "List[int]"):
    A = [0] + A
    for i in range(1, N + 1):
        A[i] = A[i] + A[i - 1]
    B = [0] + B
    for i in range(1, M + 1):
        B[i] = B[i] + B[i - 1]

    answer = 0
    for n in range(N+1):
        ka = A[n]
        if ka > K:
            break
        kb = K - ka  # ak > K だから kb >= 0  bisect_right > 0
        m = bisect_right(B, kb) - 1
        if n + m > answer:
            answer = n + m

    return answer


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    # N, M, K, A, B = map(int, line.split())
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    answer = solve(N, M, K, A, B)
    print(answer)


if __name__ == "__main__":
    main()
