import numpy as np

N = int(input())
A = list(map(int, input().split()))

A = np.argsort(A)

for a in A:
    print(a+1, end=" ")