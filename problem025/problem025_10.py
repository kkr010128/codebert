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
q = int(input())
M = list(map(int, input().split()))

can_make = [False] * 2001
for bit in range(2 ** n):
    total = 0
    for i in range(n):
        if bit & 1 << i > 0:
            total += A[i]
    if total <= 2000:
        can_make[total] = True

for m in M:
    if can_make[m]:
        print("yes")
    else:
        print("no")



