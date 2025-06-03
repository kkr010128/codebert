# -*- coding: utf-8 -*-

from collections import deque

N = int(input())
q = deque()

for i in range(N):
    lst = input().split()
    command = lst[0]
    if command == 'insert':
        q.appendleft(lst[1])
    elif command == 'delete':
        try:
            q.remove(lst[1])
        except Exception:
            pass
    elif command == 'deleteFirst':
        q.popleft()
    elif command == 'deleteLast':
        q.pop()

print(*q)