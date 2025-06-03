from collections import Counter
from itertools import accumulate

N, K = map(int,input().split())
A = list(map(int,input().split()))

d = Counter()

A = [0] + list(accumulate(A))
A = [a % K for a in A]

ans = 0
for i in range(N+1):
    ans += d[(A[i]-i) % K]
    d[(A[i]-i) % K] += 1
    if i-K+1 >= 0:
        d[(A[i-K+1] - (i-K+1)) % K] -= 1

print(ans)