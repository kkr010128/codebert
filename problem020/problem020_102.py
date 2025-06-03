from collections import deque

n = int(input())
d = deque()
cmd = ['com', 0]
for i in range(n):
    cmd = input().split()
    if cmd[0] == 'insert':
        d.appendleft(int(cmd[1]))
    elif cmd[0] == 'delete':
        try:
            d.remove(int(cmd[1]))
        except ValueError:
            pass
    elif cmd[0] == 'deleteFirst':
        d.popleft()
    elif cmd[0] == 'deleteLast':
        d.pop()
print(*list(d))