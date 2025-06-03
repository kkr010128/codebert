# import itertools
import math
# import sys
# import numpy as np

# K = int(input())
# S = input()
# n, *a = map(int, open(0))
A, B, H, M = map(int, input().split())
# H = list(map(int, input().split()))
# Q = list(map(int, input().split()))
# S = input()

# d = sorted(d.items(), key=lambda x:x[0]) # keyでsort
# all_cases = list(itertools.permutations(P))
# a = list(itertools.combinations_with_replacement([i for i in range(1, M + 1)], N))
# print(a[0][0])
# print(conditions[0])

kakudo_H = (H * 60 + M) / 720 * 360
kakudo_M = M / 60 * 360

print(math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(math.radians(abs(kakudo_H - kakudo_M)))))