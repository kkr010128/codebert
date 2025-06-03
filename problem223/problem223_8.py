from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools
from collections import deque

n,k = [int(x) for x in stdin.readline().rstrip().split()]
p = [(int(x)+1)/2 for x in stdin.readline().rstrip().split()]

m = sum(p[0:k])
maxm = m

for i in range(1,n-k+1):
    m = m - p[i-1] + p[i+k-1]
    maxm = max([maxm,m])

print(maxm)


