# -*- coding: utf-8 -*-
"""
C - Snack
https://atcoder.jp/contests/abc148/tasks/abc148_c

"""
import sys


from fractions import gcd

def solve(A, B):
    return A * B // gcd(A, B)


def main(args):
    A, B = map(int, input().split())
    ans = solve(A, B)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
