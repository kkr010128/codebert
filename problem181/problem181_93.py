from collections import deque

K = int(input())

queue = deque(range(1, 10))

for _ in range(K):
    x = queue.popleft()
    if x % 10 != 0:
        queue.append(10 * x + x % 10 - 1)
    queue.append(10 * x + x % 10)
    if x % 10 != 9:
        queue.append(10 * x + x % 10 + 1)

print(x)
