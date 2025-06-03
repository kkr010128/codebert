from collections import deque
import sys
n = int(sys.stdin.readline())
#lines = sys.stdin.readlines()
lines = [input() for i in range(n)]

deq = deque()
for i in range(n):
    o = lines[i].split()
    if o[0] == 'insert':
        deq.appendleft(o[1])
    elif o[0] == 'delete':
        try:
            deq.remove(o[1])
        except:
            continue
    elif o[0] == 'deleteFirst':
        deq.popleft()
    elif o[0] == 'deleteLast':
        deq.pop()

print(' '.join(deq))
