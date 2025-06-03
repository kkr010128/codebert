# -*- coding:utf8 -*-

from collections import deque
n = int(input())
c = [input() for _ in range(n)]
d = deque()

for com in c:
    if com[0] == 'i':
        d.appendleft(com[7:])
    else:
        s = com[6]
        if s == 'F':
            d.popleft()
        elif s == 'L':
            d.pop()
        else:
            try:
                d.remove(com[7:])
            except ValueError:
                pass
print(' '.join(d))

