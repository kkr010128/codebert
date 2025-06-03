from collections import deque
que = deque()

n = int(input())
for _ in range(n):
    command = input()
    if command == 'deleteFirst':
        que.popleft()
    elif command == 'deleteLast':
        que.pop()
    else:
        x, y = command.split()
        if x == 'insert':
            que.appendleft(int(y))
        elif int(y) in que:
            que.remove(int(y))

print(' '.join(map(str, que)))
