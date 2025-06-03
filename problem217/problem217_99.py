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

for a in A:
    if a % 2 == 0:
        if not (a % 3 == 0 or a % 5 == 0):
            print("DENIED")
            break
else:
    print("APPROVED")
