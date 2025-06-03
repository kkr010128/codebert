import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
from collections import Counter
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())

N = int(input())
A = list(map(int, input().split()))
acc = [0] * (N + 1)
for i in range(1, N + 1):
    acc[i] = acc[i - 1] + A[i - 1]

ans = INF
for i in range(1, N):
    left = acc[i]
    right = acc[-1] - acc[i]
    ans = min(ans, abs(left - right))
print(ans)
