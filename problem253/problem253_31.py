import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())

MOD = 10 ** 4 + 7

N, A, B = map(int, input().split())

if (B - A) % 2 == 0:
    print((B - A) // 2)
else:
    print(min(A - 1, N - B) + 1 + (B - A - 1) // 2)