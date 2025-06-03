# import itertools
import math
# import sys
# import numpy as np

K = int(input())
# S = input()
# n, *a = map(int, open(0))
# K, N = map(int, input().split())
# A = list(map(int, input().split()))
# Q = list(map(int, input().split()))
# S = input()

# d = sorted(d.items(), key=lambda x:x[0]) # keyでsort

tot = 0
for a in range(1, K + 1):
    for b in range(1, K + 1):
        gcd_ab = math.gcd(a, b)
        for c in range(1, K + 1):
            tot += math.gcd(gcd_ab, c)

print(tot)