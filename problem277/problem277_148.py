import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
from collections import Counter
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())

H, W, K = map(int, input().split())
A = [0] * H
for i in range(H):
    A[i] = input()

X = [[0] * W for _ in range(H)]
cur = 1
for i in range(H):
    if A[i].count('#') == 0:
        continue

    j = 0
    k = A[i].find('#')
    while j <= k:
        X[i][j] = cur
        j += 1
    while j < W:
        while j < W and A[i][j] == '.':
            X[i][j] = cur
            j += 1
        if j < W:
            cur += 1
            X[i][j] = cur
        j += 1
    cur += 1

for i in range(H - 2, -1, -1):
    for j in range(W):
        if X[i][j] == 0:
            X[i][j] = X[i + 1][j]
for i in range(1, H):
    for j in range(W):
        if X[i][j] == 0:
            X[i][j] = X[i - 1][j]

for i in range(H):
    print(*X[i])