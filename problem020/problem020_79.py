from collections import deque

n = int(input())
d = deque()

for i in range(n):
    c = input()
    if ' ' in c:
        c, num = c.split()
        if c == 'insert':
            d.appendleft(num)
        elif c == 'delete' and num in d:
            d.remove(num)
    else:
        if c == 'deleteFirst' and d:
            d.popleft()
        elif c == 'deleteLast' and d:
            d.pop()

print(' '.join(d))
