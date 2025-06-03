# -*- coding: utf-8 -*-
"""
B - TAKOYAKI FESTIVAL 2019
https://atcoder.jp/contests/abc143/tasks/abc143_b

"""
import sys


from itertools import combinations

def solve(takoyaki):
    return sum(x * y for x, y in combinations(takoyaki, 2))


def main(args):
    _ = input()
    takoyaki = map(int, input().split())
    ans = solve(takoyaki)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
