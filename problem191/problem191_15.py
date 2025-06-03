#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(L: int):
    ret = (L / 3) ** 3
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    L = int(next(tokens))  # type: int
    solve(L)

if __name__ == '__main__':
    main()
