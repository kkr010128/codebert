from collections import deque
n = int(input())
d = deque()

for i in range(n):
    line = input().split()
    if len(line) == 2:
        command, ele = line
    else:
        command = line[0]

    if command == 'insert':
        d.appendleft(ele)
    elif command == 'delete':
        if ele in d:
            d.remove(ele)
    elif command == 'deleteFirst':
        d.popleft()
    elif command == 'deleteLast':
        d.pop()

print(' '.join(list(d)))