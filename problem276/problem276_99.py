import numpy as np

N = int(input())
A = list(map(int, input().split()))

cum_A = np.cumsum(A)
ans = 10 ** 18
for i in range(N):
    left = cum_A[i]
    right = cum_A[-1] - cum_A[i]
    ans = min(ans, abs(left - right))
print(ans)
