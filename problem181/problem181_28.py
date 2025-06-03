import sys
input = sys.stdin.readline
from collections import deque

k, q = int(input()), deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
for i in range(1, k):
    x = q.popleft()
    if x % 10 != 0: q.append(10 * x + (x % 10) - 1)
    q.append(10 * x + (x % 10))
    if x % 10 != 9: q.append(10 * x + (x % 10) + 1)
print(q.popleft())