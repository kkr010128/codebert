import sys
input = sys.stdin.readline
from itertools import accumulate
N, K = map(int, input().split())
A = map(int, input().split())
B = accumulate(A)
C = [0]+[(b-i)%K for i, b in enumerate(B,start=1)]
cnt = dict()
cnt[C[0]] = 1
res = 0
for i in range(1, N+1):
    if i >= K:
        cnt[C[i-K]] = cnt.get(C[i-K],0) - 1
    res += cnt.get(C[i], 0)
    cnt[C[i]] = cnt.get(C[i],0) + 1
print(res)
