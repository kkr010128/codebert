
from collections import deque

K = int(input())
q = deque(list(range(1, 10)))
for _ in range(K - 1):
    u = q.popleft()
    n = u % 10
    for x in range(max(0, n - 1), min(9, n + 1) + 1):
        q.append(u * 10 + x)

print(q.popleft())
