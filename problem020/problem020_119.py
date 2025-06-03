from collections import deque
import sys

dlist = deque()

func = {'insert':dlist.appendleft, 'delete':dlist.remove, 'deleteFirst':dlist.popleft, 'deleteLast':dlist.pop}

n = int(sys.stdin.readline())

for line in sys.stdin:
    command = line.split()
    if len(command) == 2:
        command[1] = int(command[1])
    try:
        func[command[0]](*command[1:])
    except ValueError:
        pass

print(*dlist)