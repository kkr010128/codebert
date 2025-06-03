import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())

N = int(input())
A = list(map(int, input().split()))

cur = 1000
left = 0
right = 1
while left < N:
    while right < N and A[right] > A[right - 1]:
        right += 1
    if right - left > 1:
        stocks = cur // A[left]
        cur = cur % A[left]
        cur += A[right - 1] * stocks
    left = right
    right = left + 1
print(cur)