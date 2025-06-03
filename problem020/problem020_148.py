import sys
from collections import deque
N = int(sys.stdin.readline())
lines = sys.stdin.readlines()

l = deque()
for i in range(N):
    command = lines[i].split()
    if command[0] == 'deleteFirst':
        l.popleft()
    elif command[0] == 'deleteLast':
        l.pop()
    elif command[0] == 'insert':
        l.appendleft(command[1])
    else:
        if command[1] in l:
            l.remove(command[1])
            
print(' '.join(map(str, l)))
    
