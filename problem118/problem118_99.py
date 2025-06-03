import sys
import math
import collections
import decimal
import itertools
from collections import deque
from functools import reduce
import heapq
n = int(input())
#n, m, k = map(int, sys.stdin.readline().split())
#s = input()
#A = list(map(int, sys.stdin.readline().split()))

ans = 0
for i in range(1, n+1):
    x = n // i
    y = i * (x * (x + 1)) // 2
    ans += y

print(ans)








