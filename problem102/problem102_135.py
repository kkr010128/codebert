from functools import reduce
from operator import mul

N,K,*A = map(int,open(0).read().split())
base = sum(A[:K])
for i in range(K,N):
    score = base - A[i-K] + A[i]
    print("Yes" if base < score else "No")
    base = score