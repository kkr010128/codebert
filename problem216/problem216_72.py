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

A, B, C = map(int, input().split())
if A == B and B != C:
    print("Yes")
elif B == C and B != A:
    print("Yes")
elif C == A and C != B:
    print("Yes")
else:
    print("No")