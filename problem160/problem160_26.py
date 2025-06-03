import itertools
# import math
# import sys
# import numpy as np

# K = int(input())
# S = input()
# n, *a = map(int, open(0))
N, M, Q = map(int, input().split())
# A = list(map(int, input().split()))
# Q = list(map(int, input().split()))
# S = input()

# d = sorted(d.items(), key=lambda x:x[0]) # keyでsort

conditions = []
for i in range(Q):
    conditions.append(list(map(int, input().split())))

# all_cases = list(itertools.permutations(P))
a = list(itertools.combinations_with_replacement([i for i in range(1, M + 1)], N))
# print(a[0][0])
# print(conditions[0])

max_score = 0
for t in a:
    tot = 0
    for condition in conditions:
        if t[condition[1] - 1] - t[condition[0] - 1] == condition[2]:
            tot += condition[3]
    if tot > max_score:
        max_score = tot
print(max_score)