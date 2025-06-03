# -*- coding: utf-8 -*-


def maximum_profit(profits):
    max_v = profits[1] - profits[0]
    min_v = profits[0]

    for j in range(1, len(profits)):
        max_v = max(max_v, profits[j]-min_v)
        min_v = min(min_v, profits[j])

    print(max_v)


def to_int(v):
    return int(v)


if __name__ == '__main__':
    l = to_int(input())
    profits = [to_int(input()) for i in range(l)]

    maximum_profit(profits)