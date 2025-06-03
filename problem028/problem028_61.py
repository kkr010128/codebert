#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools as ite
import math
import random
import sys
import codecs
from collections import defaultdict

sys.setrecursionlimit(1000000)

INF = 10 ** 18
MOD = 10 ** 9 + 7

n, m = map(int, input().split())
c = list(map(int, input().split()))
DP = [0] + [n] * n
for i in range(m):
    for j in range(c[i], n + 1):
        DP[j] = min(DP[j], DP[j - c[i]] + 1)
print(DP[n])

