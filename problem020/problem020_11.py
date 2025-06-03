#!/usr/bin/env python
from __future__ import division, print_function
from sys import stdin
from collections import deque

n = int(stdin.readline())
dll = deque()
fcode = ord('F')
lcode = ord('L')
while n:
    n -= 1
    cmd = stdin.readline().rstrip()
    if cmd.startswith('i'):
        dll.appendleft(int(cmd[7:]))
    elif cmd.startswith('d'):
        c = ord(cmd[6])
        if c == fcode:
            dll.popleft()
        elif c == lcode:
            dll.pop()
        else:
            try:
                dll.remove(int(cmd[7:]))
            except ValueError:
                pass
print(*dll)