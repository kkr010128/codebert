import sys
from collections import deque

n = int(input())
ary = deque([])

for line in sys.stdin:
    op = line.strip().split()
    cmd = op[0]

    if cmd[0] == 'i':
        x = op[1]
        ary.appendleft(x)

    elif len(cmd) == 6:
        x = op[1]
        if x in ary:
            ary.remove(x)

    elif len(cmd) == 10:
        ary.pop()

    else:
        ary.popleft()

print(*ary)

