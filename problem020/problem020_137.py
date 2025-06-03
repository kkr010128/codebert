from collections import deque

n = int(input())
Q = deque()
for _ in range(n):
    query = input()
    if query=='deleteFirst':
        Q.popleft()
    elif query=='deleteLast':
        Q.pop()
    else:
        q, x = query.split()
        if q=='insert':
            Q.appendleft(x)
        else:
            try:
                Q.remove(x)
            except ValueError:
                pass

print(' '.join(Q))
