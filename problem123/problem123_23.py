import sys
import numpy as np
import math
import collections
from collections import deque 
from functools import reduce

# input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
axor = 0
for ai in a:
    axor ^= ai
ans = []
for ni in range(n):
    ans.append(str(axor ^ a[ni]))
print(" ".join(ans))
