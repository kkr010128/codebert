#! /usr/bin/env python3

import sys
import numpy as np
from itertools import groupby
int1 = lambda x: int(x) - 1
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(500000)

S = readline().decode().rstrip()
cnt = [0] * (len(S) + 1)

for i in range(len(S)):
    if S[i] == '<':
        cnt[i + 1] = max(cnt[i + 1], cnt[i] + 1)

for i in range(len(S) - 1, -1, -1):
    if S[i] == '>':
        cnt[i] = max(cnt[i], cnt[i + 1] + 1)

print(sum(cnt))