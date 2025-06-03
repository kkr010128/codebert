from collections import deque
import sys


deq = deque()

q = int(input())

for _ in range(q):
    s = input()
    if s == 'deleteFirst':
        deq.popleft()
    elif s == 'deleteLast':
        deq.pop()
    else:
        ss, num = s.split()
        if ss == 'insert':
            deq.appendleft(num)
        else:
            try:
                deq.remove(num)
            except:
                pass

print(" ".join(deq))


