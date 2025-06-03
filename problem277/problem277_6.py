import sys
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
from itertools import accumulate
from itertools import permutations
from itertools import combinations
from collections import defaultdict
from collections import Counter
import fractions
import math
from collections import deque
from bisect import bisect_left
from bisect import insort_left
import itertools
from heapq import heapify
from heapq import heappop
from heapq import heappush
import heapq
import numpy as np
INF = float("inf")
#d = defaultdict(int)
#d = defaultdict(list)
#N = int(input())
#A = list(map(int,input().split()))
#S = list(input())
#S.remove("\n")
#N,M = map(int,input().split())
#S,T = map(str,input().split())
#A = [int(input()) for _ in range(N)]
#S = [list(input())[:-1] for _ in range(N)]
#A = [list(map(int,input().split())) for _ in range(N)]
H,W,K = map(int,input().split())
P = [list(input())[:-1] for _ in range(H)]
num= 1
cur = 1
flag = [0]*H
ans = [[0]*W for _ in range(H)]
for i in range(H):
    count = 0
    li = [0]*W
    for j in range(W):
        if P[i][j] == "#":
            count += 1
    if count == 0:
        flag[i] = 1
    else:
        judge = 0
        d = 0
        for j in range(W):
            if P[i][j] == "." or d == 1:
                ans[i][j] = num
            else:
                ans[i][j] = num
                judge += 1
                if judge == count:
                    d = 1
                else:
                    num += 1
        num += 1
for i in range(H):
    if flag[i] == 0:
        index = i
        break
for i in range(index):
    flag[i] = 0
    for j in range(W):
        ans[i][j] = ans[index][j]
for i in range(H):
    if flag[i] == 1:
        for j in range(W):
            ans[i][j] = ans[i-1][j]
for i in range(H):
    print(*ans[i])