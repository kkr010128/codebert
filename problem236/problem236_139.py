#!/usr/bin/env python3

import sys, math
sys.setrecursionlimit(300000)


def solve(H: int, W: int, N: int):
    ret = min(math.ceil(N / H), math.ceil(N / W))
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    solve(H, W, N)

if __name__ == '__main__':
    main()
