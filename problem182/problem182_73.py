from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
from collections import deque, defaultdict
from itertools import combinations, permutations, combinations_with_replacement
from itertools import accumulate
from math import ceil, sqrt, pi

MOD = 10 ** 9 + 7
INF = 10 ** 18

N, K, C = map(int, input().split())
S = input()

left = [0] * N
right = [0] * N

i = 0
cnt = 0
while i < N:
    if cnt == K:
        break
    if S[i] == "o":
        cnt += 1
        left[i] = 1
        i += C + 1
    else:
        i += 1
#print(left)

S = S[::-1]
i = 0
cnt = 0
while i < N:
    if cnt == K:
        break
    if S[i] == "o":
        cnt += 1
        right[i] = 1
        i += C + 1
    else:
        i += 1
right = right[::-1]
#print(right)

left_ls, right_ls = [], []
for i in range(N):
    if left[i]:
        left_ls.append(i + 1)
    if right[i]:
        right_ls.append(i + 1)
        
for l, r in zip(left_ls, right_ls):
    if l == r:
        print(l)