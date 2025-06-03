from sys import stdin
from collections import defaultdict as dd
from collections import deque as dq
import itertools as it
from math import sqrt, log, log2
from fractions import Fraction

# t = int(stdin.readline())
# for _ in range(t):
# n, m = map(int, stdin.readline().split())
# nums = list(map(int, stdin.readline().split()))
# n = int(input())
# if n%10 in [2, 4, 5, 7, 9]:
#     print('hon')
# elif n%10 in [0, 1, 6, 8]:
#     print('pon')
# else:
#     print('bon')

k = int(input())
s = input()

ans = s[:k] + ('...' if len(s) > k else '')
print(ans)