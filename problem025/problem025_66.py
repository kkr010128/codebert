#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import print_function,division
from itertools import combinations
import time
import sys
import io
import re
import math
start = time.clock()
i = 0
def enum_sum_numbers(sets, s_range, r):
    for cmb in combinations(sets,r):
        yield sum(cmb)
    if r <=s_range:
        for s in enum_sum_numbers(sets,s_range, r+1):
            yield s

sys.stdin.readline()
a=[int(s) for s in sys.stdin.readline().split()]
sys.stdin.readline()
ms=[int(s) for s in sys.stdin.readline().split()]
sets={s for s in enum_sum_numbers(a,len(a),1)}
for m in ms:
    print('yes' if m in sets else 'no')