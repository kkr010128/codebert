# -*- coding: utf-8 -*-

from collections import deque

n = int(raw_input())
que = deque()
for i in range(n):
    com = str(raw_input())
    if com == "deleteFirst":
        del que[0]
    elif com == "deleteLast":
        del que[-1]
    else:
        c, p = com.split()
        if c == "insert":
            que.appendleft(p)
        else:
            try: que.remove(p)
            except: pass
print " ".join(map(str, que))