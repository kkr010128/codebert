
from collections import defaultdict

N, X, Y = map(int, input().split())
ctr = defaultdict(int)

for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        d = min(j - i, abs(i - X) + 1 + abs(j - Y))
        ctr[d] += 1

for i in range(1, N):
    print(ctr[i])

