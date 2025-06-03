from scipy.special import comb
from collections import Counter

N = int(input())
A = list(map(int, input().split()))
C = Counter(A)
x = 0

for c in C.values():
    x += comb(c, 2, exact=True)

for i in range(N):
    y = x - comb(C[A[i]], 2, exact=True) + comb(C[A[i]] - 1, 2, exact=True)
    print(y)
