from collections import deque
from sys import stdin
n = int(input())
ddl = deque()
for i in stdin:
    inp = i.split()
    if len(inp) == 2:
        op, data = inp
        data = int(data)
    else: op, data = inp[0], None
    if op == 'insert':
        ddl.appendleft(data,)
    elif op == 'delete':
        try:
            ddl.remove(data)
        except ValueError:
            pass
    elif op == 'deleteFirst':
        ddl.popleft()
    elif op == 'deleteLast':
        ddl.pop()

print(' '.join([str(item) for item in ddl]))