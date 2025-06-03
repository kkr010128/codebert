from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools
from collections import deque

n = int(stdin.readline().rstrip())
s = stdin.readline().rstrip()

num_r = s.count('R')
num_g = s.count('G')
num_b = s.count('B')

num_ng = 0
for i in range(n):
    for j in range(i+1,n):
        k = j+(j-i)

        if k < n and s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
            num_ng += 1

print(num_r*num_g*num_b-num_ng)