from sys import stdin, setrecursionlimit
input = stdin.buffer.readline
setrecursionlimit(10 ** 7)

from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
from collections import deque, defaultdict
from itertools import combinations, permutations, combinations_with_replacement
from itertools import accumulate
from math import ceil, sqrt, pi

MOD = 10 ** 9 + 7
INF = 10 ** 18

N, M = map(int, input().split())

arr = []
for i in range(M):
    arr.append([1, i + 2])
arr = arr[::-1]
#print(arr)

max_arr = -1
plus = 0
for a, b in arr[::2]:
    print(a + plus, b + plus)
    max_arr = max(max_arr, b + plus)
    plus += 1
#print(max_arr)

plus = 0
for a, b in arr[1::2]:
    print(max_arr + a + plus, max_arr + b + plus)
    plus += 1