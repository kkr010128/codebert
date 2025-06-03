# -*- coding: utf-8 -*-

import sys
import os
from collections import deque


N = int(sys.stdin.readline())
q = deque()

lines = sys.stdin.readlines()
for s in lines:
    lst = s.split()
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