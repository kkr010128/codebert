import sys
import math
import string
import fractions
import random
from operator import itemgetter
import itertools
from collections import deque
import copy
import heapq
import bisect

MOD = 10 ** 9 + 7
INF = float('inf')
input = lambda: sys.stdin.readline().strip()

sys.setrecursionlimit(10 ** 8)

n = int(input())
dis = [-1] * n
info = [list(map(int, input().split())) for _ in range(n)]

stack = [[0, 0]]
ans = 0
while len(stack) > 0:
    num = stack.pop(0)
    if dis[num[0]] == -1:
        dis[num[0]] = num[1]
    for i in info[num[0]][2:]:
        if dis[i-1] == -1:
            stack.append([i - 1, num[1] + 1])
for i in range(n):
    print(str(i+1) + " " + str(dis[i]))

