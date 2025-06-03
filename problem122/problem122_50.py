
from collections import Counter

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
X = [list(map(int, input().split())) for _ in range(Q)]

ctr = Counter(A)
ans = sum(A)
for b, c in X:
    n = ctr[b]
    ans += -b * n + c * n
    ctr[b] = 0
    ctr[c] += n
    print(ans)
