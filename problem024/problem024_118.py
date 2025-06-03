# -*- coding:utf-8 -*-
import sys


def allcation(truck, baggage, limit):
    t = 1
    cap = 0
    for weight in baggage:
        if weight <= limit:
            if cap + weight <= limit:
                cap += weight
            else:
                cap = weight
                t += 1

            if t > truck:
                return False
        else:
            return False
    return True


def bin_search(truck, baggage):
    small = 0
    big = 10000 * 100000
    minimum = 0
    while small < big:
        mid = (small + big) >> 1
        if allcation(truck, baggage, mid):
            big = mid
            minimum = mid
        else:
            small = mid + 1

    return minimum


if __name__ == "__main__":
    n = [int(val) for val in input().split()]
    lst = [int(val) for val in sys.stdin.read().splitlines()]
    print(bin_search(n[1], lst))