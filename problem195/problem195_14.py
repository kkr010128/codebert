import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
from bisect import *
from collections import *
from heapq import *
INF = 500000
mod = 10**9+7

l = [1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51]
K = int(input())-1
print(l[K])

# a, b, c = input(), input(), input()
# la, lb, lc = len(a), len(b), len(c)
# for i in range(1, min(la, lb)):
#     S = ''
#     for j in range(i):
#         if a[la-i+j] == b[j]:
#             S += b[j]
#             continue
#         elif a[la-i+j] == '?':
#             S += b[j]
#         elif b[j] == '?':
#             S += c[j]
