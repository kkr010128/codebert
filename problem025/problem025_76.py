#!/usr/bin/env python
from __future__ import division, print_function
from sys import stdin
from itertools import combinations


def enum_sum_numbers(sets, s_range, r):
    for cmb in combinations(sets, r):
        yield sum(cmb)
    if r <= s_range:
        for s in enum_sum_numbers(sets, s_range, r+1):
            yield s


stdin.readline()
a = [int(s) for s in stdin.readline().split()]
stdin.readline()
ms = [int(s) for s in stdin.readline().split()]
sets = {s for s in enum_sum_numbers(a, len(a), 1)}

for m in ms:
    print('yes' if m in sets else 'no')