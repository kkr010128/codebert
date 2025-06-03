#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
input:
15 6
1 2 7 8 12 50

output:
2
"""

import sys


def solve():
    rec[0] = 0
    for i in range(c_num):
        for j in range(money - coins[i] + 1):
            rec[j + coins[i]] = min(rec[j + coins[i]], rec[j] + 1)

    return rec


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    money, c_num = map(int, _input[0].split())
    coins = list(map(int, _input[1].split()))
    assert len(coins) == c_num
    rec = [float('inf')] * (money + 1)
    ans = solve()
    print(ans[-1])