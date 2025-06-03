# -*- coding: utf-8 -*-
"""
A - Can't Wait for Holiday
https://atcoder.jp/contests/abc146/tasks/abc146_a

"""
import sys


def solve(S):
    return {'SUN': 7, 'MON': 6, 'TUE': 5, 'WED': 4, 'THU': 3, 'FRI': 2, 'SAT': 1}[S]


def main(args):
    S = input()
    ans = solve(S)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
