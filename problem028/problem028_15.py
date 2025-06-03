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

n, m = map(int, input().split())
C = list(map(int, input().split()))

MAX = 10 ** 5
dp = [MAX] * (n + 1)

dp[0] = 0
for i in range(m):
    c = C[i]
    for j in range(n + 1):
        if j >= c:
            dp[j] = min(dp[j], dp[j - c] + 1)
print(dp[n])

