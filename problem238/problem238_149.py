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

N, K, S = map(int, input().split())

if S == 10 ** 9:
    for i in range(N):
        if i < N - K:
            print(S - 1)
        else:
            print(S)
    exit()

for i in range(N):
    if i < K:
        print(S)
    else:
        print(S + 1)
