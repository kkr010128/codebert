# import itertools
# import math
# import sys
import numpy as np

# N = int(input())
# S = input()
# n, *a = map(int, open(0))
N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
# S = input()

# d = sorted(d.items(), key=lambda x:x[0]) # keyでsort
# all_cases = list(itertools.permutations(P))
# a = list(itertools.combinations_with_replacement([i for i in range(1, M + 1)], N))
# print(a[0][0])
# print(conditions[0])

A = np.array(A)
B = np.array(B)

cum_A = np.cumsum(A)
cum_A = np.insert(cum_A, 0, 0)
cum_B = np.cumsum(B)
cum_B = np.insert(cum_B, 0, 0)

j = M
max_num = 0
for i in range(N + 1):
    while(True):
        # j -= 1
        if j < 0:
            break
        minute = cum_A[i] + cum_B[j]
        if minute <= K:
            if i + j > max_num:
                max_num = i + j
            break
        j -= 1

print(max_num)