
from collections import defaultdict
from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

ctr = defaultdict(list)
for i in range(N):
    ctr[i + A[i]].append(i)

ans = 0
for i in range(N):
    v = i - A[i]
    if v in ctr:
        ans += bisect_left(ctr[v], i)

print(ans)
