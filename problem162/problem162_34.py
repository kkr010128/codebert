n, m = map(int, input().split())

from collections import deque

l = deque([i for i in range(1, n + 1)])

if n % 2 ==0:
    for i in range(1, m + 1):
        a, b = l.popleft(), l.pop()
        if (b - a) == n / 2 or (len(l) < n // 2 and (b-a) % 2 == 1):
            b = l.pop()
        print(a, b)
else:
    for i in range(1, m + 1):
        print(i, n - i)