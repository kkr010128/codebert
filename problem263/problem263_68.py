import sys
import itertools
# import numpy as np
import time
import math

sys.setrecursionlimit(10 ** 7)

from collections import defaultdict

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(input())
A = list(map(int, input().split()))

MOD = 10 ** 9 + 7

x = 1
ans = 0
for i in range(60):
    ones = 0
    zeros = 0
    for a in A:
        if a & (1 << i) > 0:
            ones += 1
        else:
            zeros += 1
    ans += (ones * zeros * x) % MOD
    x *= 2

print(ans % MOD)

