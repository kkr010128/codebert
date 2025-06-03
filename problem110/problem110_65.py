#!/usr/bin/env python3
import sys
from itertools import combinations as comb
from itertools import chain
import numpy as np

# form bisect import bisect_left, bisect_right, insort_left, insort_right
# from collections import Counter


def solve(H, W, K, C):
    answer = 0
    for hn in range(H + 1):
        for wn in range(W + 1):
            for h_idxs in comb(range(H), hn):
                for w_idxs in comb(range(W), wn):
                    cs = C.copy()
                    cs[h_idxs, :] = 0
                    cs[:, w_idxs] = 0
                    answer += cs.sum() == K
    return answer


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    H = int(next(tokens))
    W = int(next(tokens))
    K = int(next(tokens))
    C = np.array(
        [
            list(map(lambda x: {"#": 1, ".": 0}[x], line))
            for line in tokens
        ]
    )
    answer = solve(H, W, K, C)
    print(answer)


if __name__ == "__main__":
    main()
