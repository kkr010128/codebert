import sys
from collections import deque
 
n = int(sys.stdin.readline())
que = deque()
for i in range(n):
    line = sys.stdin.readline()
    op = line.rstrip().split()
    if "insert" == op[0]:
        que.appendleft(op[1])
    elif "delete" == op[0]:
        if op[1] in que:
            que.remove(op[1])
    elif "deleteFirst" == op[0]:
        que.popleft()
    else:
        que.pop()
 
print(*que)