from collections import deque
import sys

dq = deque()
num = int(sys.stdin.readline())
line = sys.stdin.readlines()

for i in range(num):

    order = line[i].split()

    if order[0] == 'insert':
        dq.appendleft(order[1])
    elif order[0] == 'deleteFirst':
        dq.popleft()
    elif order[0] == 'deleteLast':
        dq.pop()
    else:
        if order[1] in dq:
            dq.remove(order[1])

print(' '.join(dq))