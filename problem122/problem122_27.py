import numpy as np

from collections import defaultdict
N = int(input())
A = tuple(map(int, input().split()))
Q = int(input())
BC= [list(map(int,input().split())) for _ in range(Q)]

counter = defaultdict(int)
for x in A:
    counter[x] += 1

total = sum(A)
for b, c in BC:
    total += (c - b) * counter[b]
    counter[c] += counter[b]
    counter[b] = 0
    print(total)
