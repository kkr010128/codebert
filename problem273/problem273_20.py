from collections import defaultdict as dd
from itertools import accumulate
N, K = map(int, input().split())
As = [0] + list(map(int, input().split()))
S = list(accumulate(As))

ans = 0
counts = dd(int)
counts[0] = 1
for j in range(1, N+1):
    if j >= K:
        counts[(S[j-K] - (j-K)) % K] -= 1
    t = (S[j] - j) % K
    ans += counts[t]
    counts[t] += 1
print(ans)