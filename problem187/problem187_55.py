from collections import deque
from collections import Counter
N, X, Y = map(int, input().split())

res = deque()

for x in range(1, N):
    for y in range(x + 1, N+1):
        res.append(min(abs(x-y), 1 + abs(X-x) + abs(Y-y)))
resd = Counter(res)

for i in range(1, N):
    if i in resd.keys():
        print(resd[i])
    else:
        print(0)