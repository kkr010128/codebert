from functools import reduce
from collections import deque


def operate(dq, op):
    if op[0] == 'i':
        dq.appendleft(int(op[7:]))
    else:
        k = op[6]
        if k == 'F':
            dq.popleft()
        elif k == 'L':
            dq.pop()
        else:
            try:
                dq.remove(int(op[7:]))
            except ValueError:
                pass
    return dq


n = int(input())
print(*reduce(operate, [input() for _ in range(n)], deque()))