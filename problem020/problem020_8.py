from collections import deque
n = int(input())
d = deque()
for i in range(n):
    cmd = input().split()
    if cmd[0] == 'insert':
        d.appendleft(cmd[1])
    elif cmd[0] == 'delete':
        try:
            d.remove(cmd[1])
        except:
            pass
    elif cmd[0] == 'deleteFirst':
        d.popleft()
    elif cmd[0] == 'deleteLast':
        d.pop()
print(' '.join(d))
