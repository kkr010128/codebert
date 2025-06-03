# -*- coding: utf-8 -*-
"""
A - 9x9
https://atcoder.jp/contests/abc144/tasks/abc144_a

"""
import sys


def solve(A, B):
    if 1 <= A <= 9 and 1 <= B <= 9:
        return A * B
    return -1


def main(args):
    A, B = map(int, input().split())
    ans = solve(A, B)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
