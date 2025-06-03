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
    for coin in coins:
        for current_cost in range(coin, total_cost + 1):
            rec[current_cost] = min(rec[current_cost], rec[current_cost - coin * 1] + 1)

    return rec


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    total_cost, c_num = map(int, _input[0].split())
    coins = list(map(int, _input[1].split()))
    # assert len(coins) == c_num
    rec = [float('inf')] * (total_cost + 1)
    ans = solve()
    print(ans[-1])