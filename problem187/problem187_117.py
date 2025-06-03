
from collections import defaultdict

N, X, Y = map(int, input().split())

ctr = defaultdict(int)
for u in range(1, N):
    for v in range(u + 1, N + 1):
        d = min(v - u, abs(u - X) + 1 + abs(Y - v))
        ctr[d] += 1

for n in range(1, N):
    print(ctr[n])
