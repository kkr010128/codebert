from collections import deque

n = int(input())
q = deque(range(1, 10))
for _ in range(n - 1):
    x = q.popleft()
    r = x % 10
    y = 10 * x
    if r == 0:
        q.extend([y, y+1])
    elif r == 9:
        q.extend([y+8, y+9])
    else:
        q.extend([y+r-1, y+r, y+r+1])
print(q.popleft())