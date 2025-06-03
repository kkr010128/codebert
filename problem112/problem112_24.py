#!/usr/bin/python3
import sys
from functools import reduce
from operator import mul
input = lambda: sys.stdin.readline().strip()
n, k = [int(x) for x in input().split()]
a = sorted((int(x) for x in input().split()), key=abs)
sgn = [0 if x == 0 else x // abs(x) for x in a]
M = 10**9 + 7
def modmul(x, y):
    return x * y % M
if reduce(mul, sgn[-k:]) >= 0:
    print(reduce(modmul, a[-k:], 1))
else:
    largest_unselected_neg = next(i for i, x in enumerate(reversed(a[:-k])) if x < 0) if any(x < 0 for x in a[:-k]) else None
    largest_unselected_pos = next(i for i, x in enumerate(reversed(a[:-k])) if x > 0) if any(x > 0 for x in a[:-k]) else None
    smallest_selected_neg = next(i for i, x in enumerate(a[-k:]) if x < 0) if any(x < 0 for x in a[-k:]) else None
    smallest_selected_pos = next(i for i, x in enumerate(a[-k:]) if x > 0) if any(x > 0 for x in a[-k:]) else None
    can1 = largest_unselected_neg is not None and smallest_selected_pos is not None
    can2 = largest_unselected_pos is not None and smallest_selected_neg is not None
    def ans1():
        return list(reversed(a[:-k]))[largest_unselected_neg] * reduce(modmul, (x for i, x in enumerate(a[-k:]) if i != smallest_selected_pos), 1) % M 
    def ans2():
        return list(reversed(a[:-k]))[largest_unselected_pos] * reduce(modmul, (x for i, x in enumerate(a[-k:]) if i != smallest_selected_neg), 1) % M
    if can1 and not can2:
        print(ans1())
    elif can2 and not can1:
        print(ans2())
    elif can1 and can2:
        if list(reversed(a[:-k]))[largest_unselected_neg] * a[-k:][smallest_selected_neg] > list(reversed(a[:-k]))[largest_unselected_pos] *  a[-k:][smallest_selected_pos]:
            print(ans1())
        else:
            print(ans2())
    else:
        print(reduce(modmul, a[:k], 1))