from itertools import accumulate
from collections import defaultdict
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = accumulate([0]+ A)
C = [(b-i)%K for i, b in enumerate(B)]
cnt = defaultdict(int)
cnt[C[0]] = 1
res = 0
for i in range(1, N+1):
    if i >= K:
        cnt[C[i-K]] -= 1
    res += cnt[C[i]]
    cnt[C[i]] += 1
print(res)
