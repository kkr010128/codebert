#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
input:
6
5
3
1
3
4
3

output:
3
"""

import sys


def solve():
    # write your code here
    max_profit = -1 * float('inf')
    min_stock = prices[0]
    for price in prices[1:]:
        max_profit = max(max_profit, price - min_stock)
        min_stock = min(min_stock, price)
    return max_profit


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    p_num = int(_input[0])
    prices = list(map(int, _input[1:]))
    print(solve())